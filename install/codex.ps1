$ErrorActionPreference = "Stop"

$SourceAdapterRel = Join-Path (Join-Path (Join-Path "agents" "skills") "dare-research-engine") "SKILL.md"
$CodexAdapterRel = Join-Path (Join-Path (Join-Path ".agents" "skills") "dare-research-engine") "SKILL.md"
$RequiredRootSkill = Join-Path "de-anthropocentric-research-engine" "SKILL.md"
$RequiredCatalogSkill = Join-Path "research-catalog" "SKILL.md"

function Show-Usage {
@"
Usage: ./install/codex.ps1 [options]

Install the DARE Codex adapter from this cloned repository into a target project.

Options:
  --target <dir>   Project directory to install into (default: current directory)
  --copy           Copy the DARE skills knowledge base into .dare/skills
  --link           Symlink .dare/skills to this clone's skills directory
  --force          Replace an existing adapter file
  --dry-run        Show what would change without writing files
  -h, --help       Show this help

Default behavior copies the knowledge base so the target still works if this clone is removed.
"@
}

function Stop-WithUsage([string]$Message) {
  [Console]::Error.WriteLine("dare-codex-install: $Message")
  [Console]::Error.WriteLine("")
  [Console]::Error.WriteLine((Show-Usage))
  exit 1
}

function Get-ResolvedPathOrNull([string]$Path) {
  $item = Resolve-Path -LiteralPath $Path -ErrorAction SilentlyContinue
  if ($null -eq $item) {
    return $null
  }
  return $item.ProviderPath
}

function Test-SamePath([string]$Left, [string]$Right) {
  $resolvedLeft = Get-ResolvedPathOrNull $Left
  $resolvedRight = Get-ResolvedPathOrNull $Right
  if ($null -eq $resolvedLeft -or $null -eq $resolvedRight) {
    return $false
  }
  if ([System.IO.Path]::DirectorySeparatorChar -eq '\') {
    return [string]::Equals($resolvedLeft, $resolvedRight, [System.StringComparison]::OrdinalIgnoreCase)
  }
  return [string]::Equals($resolvedLeft, $resolvedRight, [System.StringComparison]::Ordinal)
}

function Test-SameFileContent([string]$Left, [string]$Right) {
  if (-not (Test-Path -LiteralPath $Left -PathType Leaf) -or -not (Test-Path -LiteralPath $Right -PathType Leaf)) {
    return $false
  }
  $leftHash = (Get-FileHash -LiteralPath $Left -Algorithm SHA256).Hash
  $rightHash = (Get-FileHash -LiteralPath $Right -Algorithm SHA256).Hash
  return $leftHash -eq $rightHash
}

function Assert-DareSkillsRoot([string]$Root) {
  $rootSkill = Join-Path $Root $RequiredRootSkill
  $catalogSkill = Join-Path $Root $RequiredCatalogSkill
  if (-not (Test-Path -LiteralPath $rootSkill -PathType Leaf)) {
    Stop-WithUsage "Existing skills root is not a DARE skills tree: missing $rootSkill"
  }
  if (-not (Test-Path -LiteralPath $catalogSkill -PathType Leaf)) {
    Stop-WithUsage "Existing skills root is not a DARE skills tree: missing $catalogSkill"
  }
}

function Copy-Skills([string]$Source, [string]$Dest) {
  $parent = Split-Path -Parent $Dest
  New-Item -ItemType Directory -Force -Path $parent | Out-Null
  Copy-Item -LiteralPath $Source -Destination $parent -Recurse
}

$TargetDir = (Get-Location).Path
$Mode = "copy"
$ForceInstall = $false
$DryRun = $false

for ($i = 0; $i -lt $args.Count; $i++) {
  switch ($args[$i]) {
    "--target" {
      $i++
      if ($i -ge $args.Count) {
        Stop-WithUsage "--target requires a directory"
      }
      $TargetDir = $args[$i]
    }
    "--copy" { $Mode = "copy" }
    "--link" { $Mode = "link" }
    "--force" { $ForceInstall = $true }
    "--dry-run" { $DryRun = $true }
    "-h" {
      Show-Usage
      exit 0
    }
    "--help" {
      Show-Usage
      exit 0
    }
    default {
      Stop-WithUsage "Unknown option: $($args[$i])"
    }
  }
}

if ($Mode -notin @("copy", "link")) {
  Stop-WithUsage "Invalid mode: $Mode"
}

if (-not (Test-Path -LiteralPath $TargetDir -PathType Container)) {
  Stop-WithUsage "Target directory does not exist: $TargetDir"
}

$TargetDir = (Resolve-Path -LiteralPath $TargetDir).ProviderPath
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = (Resolve-Path -LiteralPath (Join-Path $ScriptDir "..")).ProviderPath
$SourceAdapter = Join-Path $RepoRoot $SourceAdapterRel
$SourceSkills = Join-Path $RepoRoot "skills"

if (-not (Test-Path -LiteralPath $SourceAdapter -PathType Leaf)) {
  Stop-WithUsage "Codex adapter not found at $SourceAdapter"
}
Assert-DareSkillsRoot $SourceSkills

$DestAdapter = Join-Path $TargetDir $CodexAdapterRel
$AdapterStatus = "created"

if (Test-Path -LiteralPath $DestAdapter -PathType Leaf) {
  if (Test-SameFileContent $SourceAdapter $DestAdapter) {
    $AdapterStatus = "unchanged"
  } else {
    if (-not $ForceInstall) {
      Stop-WithUsage "Adapter already exists and differs: $DestAdapter. Re-run with --force to replace it."
    }
    $AdapterStatus = "replaced"
  }
}

if ($AdapterStatus -eq "created" -or $AdapterStatus -eq "replaced") {
  if ($DryRun) {
    if ($AdapterStatus -eq "created") {
      $AdapterStatus = "would-create"
    } else {
      $AdapterStatus = "would-replace"
    }
  } else {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $DestAdapter) | Out-Null
    Copy-Item -LiteralPath $SourceAdapter -Destination $DestAdapter -Force
  }
}

$SkillsPath = $SourceSkills
$SkillsStatus = "using-repo-skills"
$SkillsSource = $null
$LinkFallbackReason = $null

if (-not (Test-SamePath $RepoRoot $TargetDir)) {
  $DestSkills = Join-Path (Join-Path $TargetDir ".dare") "skills"
  $SkillsPath = $DestSkills

  if (Test-Path -LiteralPath $DestSkills) {
    if (-not (Test-Path -LiteralPath $DestSkills -PathType Container)) {
      Stop-WithUsage "Existing DARE skills path is not a directory: $DestSkills"
    }
    Assert-DareSkillsRoot $DestSkills
    if (Test-SamePath $SourceSkills $DestSkills) {
      $SkillsStatus = "linked-existing"
    } else {
      $SkillsStatus = "existing-dare-skills"
    }
  } elseif ($DryRun) {
    if ($Mode -eq "link") {
      $SkillsStatus = "would-link"
    } else {
      $SkillsStatus = "would-copy"
    }
  } elseif ($Mode -eq "copy") {
    Copy-Skills $SourceSkills $DestSkills
    $SkillsStatus = "copied"
  } else {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $DestSkills) | Out-Null
    try {
      $itemType = "SymbolicLink"
      if ([System.IO.Path]::DirectorySeparatorChar -eq '\') {
        $itemType = "Junction"
      }
      New-Item -ItemType $itemType -Path $DestSkills -Target $SourceSkills | Out-Null
      $SkillsStatus = "linked"
      $SkillsSource = $SourceSkills
    } catch {
      if ($Mode -eq "link") {
        Stop-WithUsage "Could not create symlink $DestSkills -> $SourceSkills: $($_.Exception.Message)"
      }
      Copy-Skills $SourceSkills $DestSkills
      $SkillsStatus = "copied-fallback"
      $LinkFallbackReason = $_.Exception.Message
    }
  }
}

Write-Output "dare-codex-install:"
if ($DryRun) {
  Write-Output "  dry_run: true"
}
Write-Output "  repo: $RepoRoot"
Write-Output "  target: $TargetDir"
Write-Output "  adapter: $AdapterStatus $DestAdapter"
Write-Output "  skills: $SkillsStatus $SkillsPath"
if ($null -ne $SkillsSource) {
  Write-Output "  skills_source: $SkillsSource"
}
if ($null -ne $LinkFallbackReason) {
  Write-Output "  link_fallback_reason: $LinkFallbackReason"
}
Write-Output '  invoke: $dare-research-engine'
Write-Output "  mcp: not configured by this installer"
