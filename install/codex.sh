#!/usr/bin/env sh
set -eu

SOURCE_ADAPTER_REL='agents/skills/dare-research-engine/SKILL.md'
CODEX_ADAPTER_REL='.agents/skills/dare-research-engine/SKILL.md'
REQUIRED_ROOT_SKILL='de-anthropocentric-research-engine/SKILL.md'
REQUIRED_CATALOG_SKILL='research-catalog/SKILL.md'

usage() {
  cat <<'EOF'
Usage: ./install/codex.sh [options]

Install the DARE Codex adapter from this cloned repository into a target project.

Options:
  --target <dir>   Project directory to install into (default: current directory)
  --copy           Copy the DARE skills knowledge base into .dare/skills
  --link           Symlink .dare/skills to this clone's skills directory
  --force          Replace an existing adapter file
  --dry-run        Show what would change without writing files
  -h, --help       Show this help

Default behavior copies the knowledge base so the target still works if this clone is removed.
EOF
}

die() {
  printf 'dare-codex-install: %s\n\n' "$1" >&2
  usage >&2
  exit 1
}

abs_dir() {
  (CDPATH= cd -P "$1" 2>/dev/null && pwd) || return 1
}

same_dir() {
  left=$(abs_dir "$1") || return 1
  right=$(abs_dir "$2") || return 1
  [ "$left" = "$right" ]
}

dirname_of() {
  dirname "$1"
}

validate_skill_root() {
  root=$1
  [ -f "$root/$REQUIRED_ROOT_SKILL" ] || die "Existing skills root is not a DARE skills tree: missing $root/$REQUIRED_ROOT_SKILL"
  [ -f "$root/$REQUIRED_CATALOG_SKILL" ] || die "Existing skills root is not a DARE skills tree: missing $root/$REQUIRED_CATALOG_SKILL"
}

copy_skills() {
  source=$1
  dest=$2
  parent=$(dirname_of "$dest")
  mkdir -p "$parent"
  cp -R "$source" "$dest"
}

script_dir=$(CDPATH= cd -P "$(dirname "$0")" && pwd)
repo_root=$(CDPATH= cd -P "$script_dir/.." && pwd)
target_dir=$(pwd)
mode='copy'
force=0
dry_run=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      shift
      [ "$#" -gt 0 ] || die '--target requires a directory'
      target_dir=$1
      ;;
    --copy)
      mode='copy'
      ;;
    --link)
      mode='link'
      ;;
    --force)
      force=1
      ;;
    --dry-run)
      dry_run=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "Unknown option: $1"
      ;;
  esac
  shift
done

case "$mode" in
  copy|link) ;;
  *) die "Invalid mode: $mode" ;;
esac

target_dir=$(abs_dir "$target_dir") || die "Target directory does not exist: $target_dir"

source_adapter="$repo_root/$SOURCE_ADAPTER_REL"
source_skills="$repo_root/skills"

[ -f "$source_adapter" ] || die "Codex adapter not found at $source_adapter"
validate_skill_root "$source_skills"

dest_adapter="$target_dir/$CODEX_ADAPTER_REL"
adapter_status='created'

if [ -f "$dest_adapter" ]; then
  if cmp -s "$source_adapter" "$dest_adapter"; then
    adapter_status='unchanged'
  else
    [ "$force" -eq 1 ] || die "Adapter already exists and differs: $dest_adapter. Re-run with --force to replace it."
    adapter_status='replaced'
  fi
fi

if [ "$adapter_status" = 'created' ] || [ "$adapter_status" = 'replaced' ]; then
  if [ "$dry_run" -eq 1 ]; then
    if [ "$adapter_status" = 'created' ]; then
      adapter_status='would-create'
    else
      adapter_status='would-replace'
    fi
  else
    mkdir -p "$(dirname_of "$dest_adapter")"
    cp "$source_adapter" "$dest_adapter"
  fi
fi

skills_path="$source_skills"
skills_status='using-repo-skills'
skills_source=''
link_fallback_reason=''

if ! same_dir "$repo_root" "$target_dir"; then
  dest_skills="$target_dir/.dare/skills"
  skills_path="$dest_skills"

  if [ -e "$dest_skills" ]; then
    [ -d "$dest_skills" ] || die "Existing DARE skills path is not a directory: $dest_skills"
    validate_skill_root "$dest_skills"
    if same_dir "$source_skills" "$dest_skills"; then
      skills_status='linked-existing'
    else
      skills_status='existing-dare-skills'
    fi
  elif [ "$dry_run" -eq 1 ]; then
    if [ "$mode" = 'link' ]; then
      skills_status='would-link'
    else
      skills_status='would-copy'
    fi
  elif [ "$mode" = 'copy' ]; then
    copy_skills "$source_skills" "$dest_skills"
    skills_status='copied'
  else
    mkdir -p "$(dirname_of "$dest_skills")"
    if ln -s "$source_skills" "$dest_skills" 2>/tmp/dare-codex-ln.err; then
      skills_status='linked'
      skills_source="$source_skills"
    else
      link_error=$(cat /tmp/dare-codex-ln.err 2>/dev/null || true)
      rm -f /tmp/dare-codex-ln.err
      if [ "$mode" = 'link' ]; then
        die "Could not create symlink $dest_skills -> $source_skills: $link_error"
      fi
      copy_skills "$source_skills" "$dest_skills"
      skills_status='copied-fallback'
      link_fallback_reason=$link_error
    fi
    rm -f /tmp/dare-codex-ln.err
  fi
fi

printf 'dare-codex-install:\n'
[ "$dry_run" -eq 1 ] && printf '  dry_run: true\n'
printf '  repo: %s\n' "$repo_root"
printf '  target: %s\n' "$target_dir"
printf '  adapter: %s %s\n' "$adapter_status" "$dest_adapter"
printf '  skills: %s %s\n' "$skills_status" "$skills_path"
[ -n "$skills_source" ] && printf '  skills_source: %s\n' "$skills_source"
[ -n "$link_fallback_reason" ] && printf '  link_fallback_reason: %s\n' "$link_fallback_reason"
printf '  invoke: $dare-research-engine\n'
printf '  mcp: not configured by this installer\n'
