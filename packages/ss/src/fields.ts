const BASE_PAPER_FIELDS = [
  'title', 'abstract', 'year', 'authors', 'citationCount',
  'influentialCitationCount', 'referenceCount', 'isOpenAccess',
  'openAccessPdf', 'externalIds', 'fieldsOfStudy', 'publicationTypes',
  'publicationDate', 'venue', 'url',
];

// tldr is only supported by /paper/{id}, /paper/batch, /paper/search
export const PAPER_FIELDS = [...BASE_PAPER_FIELDS, 'tldr'].join(',');

// For endpoints that do NOT support tldr (recommendations, author papers)
export const PAPER_FIELDS_NO_TLDR = BASE_PAPER_FIELDS.join(',');

export const CITATION_EDGE_FIELDS = [
  'contexts', 'intents', 'isInfluential',
].join(',');

export const CITED_PAPER_FIELDS = [
  'title', 'abstract', 'year', 'authors', 'citationCount',
  'externalIds', 'url',
].join(',');

export const AUTHOR_FIELDS = [
  'name', 'affiliations', 'homepage', 'paperCount',
  'citationCount', 'hIndex', 'externalIds', 'url',
].join(',');
