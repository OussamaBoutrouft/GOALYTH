# Goalyth — Football Data Analytics Platform

Plateforme SaaS d’analyse football (web + mobile + assistant IA), alimentée par **StatsBomb Open Data**.

## Monorepo (Step 1)

- `apps/web` — Next.js (App Router) + React + TypeScript + Tailwind + shadcn/ui
- `apps/api` — Fastify + TypeScript (Drizzle pour `app`, SQL paramétré pour analytics)
- `packages/ui` — design system, tokens, composants partagés (`<Logo />`, `<Pitch />`, primitives)
- `packages/types` — types domaine StatsBomb-like + schémas Zod partagés
- `packages/stats` — utilitaires stats/coords (régression, percentiles, per-90, z-scores) + tests
- `packages/config` — configs partagées (Tailwind/TS/ESLint)
- `data/mock` — données mock StatsBomb-like + service layer (switchable vers l’API réelle)
- `db/`, `docs/`, `sql/` — schémas PostgreSQL, docs, requêtes analytiques (existants)
- `ingestion/` — pipeline d’ingestion Python (conservé à cet emplacement pour l’instant)

## Prérequis

- Node.js LTS + pnpm (`corepack enable && corepack prepare pnpm@latest --activate`, ou `corepack pnpm ...`)
- Python 3.11+ (ingestion)
- Docker (Postgres local, Redis optionnel)

## Démarrage rapide (web/app)

```bash
pnpm install
cp .env.example .env
pnpm dev          # web + api
# pnpm dev:web    # http://localhost:3000
# pnpm dev:api    # http://localhost:4000
```

### Base de données (existante)

```bash
docker compose up -d                  # postgres:16 sur localhost:5433 (db: goalyth)
docker compose --profile cache up -d  # + redis optionnel
```

### Ingestion StatsBomb (Python, inchangé)

L’ingestion reste dans `ingestion/` (voir `docs/` et `db/migrations/`). Depuis la racine :

```bash
pnpm ingest -- --competition 43 --season 3
# équivalent : python ingestion/ingest.py --competition 43 --season 3
```

> `data/open-data.zip` présent est invalide ; la récupération du dataset StatsBomb sera traitée séparément. Voir `docs/OPEN_DATA_LIMITS.md`.

## Qualité

```bash
pnpm lint
pnpm typecheck
pnpm test
pnpm build
```

## Attribution StatsBomb (OBLIGATOIRE)

Les données proviennent de [StatsBomb Open Data](https://github.com/statsbomb/open-data) sous licence CC BY 4.0.
Toute publication de données doit afficher le logo/crédit StatsBomb (`SHOW_STATSBOMB_ATTRIBUTION=true`, `AttributionBadge`).

## Documentation data

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md)
- [`docs/OPEN_DATA_LIMITS.md`](docs/OPEN_DATA_LIMITS.md)
- [`sql/sample_queries.sql`](sql/sample_queries.sql)
