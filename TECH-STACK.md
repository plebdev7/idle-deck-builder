# Tech Stack - Idle Deck Builder

**Document Version:** 1.0  
**Date:** 2025-11-04  
**Status:** Recommended Stack (Pending Final Validation)

---

## Decision Context

### Project Requirements
- **Primary:** Fully offline single-player experience
- **Secondary:** Optional future web-connected version (leaderboards, sync, multiplayer)
- **Performance:** Must be performant and run on any device
- **Development:** Pro Python developer, open to learning new tech
- **Budget:** Willing to pay for hosting if value-add is there

### Design Constraints
- Abstract visuals emphasizing performance
- Complex game logic (card interactions, combat simulation, resource generation)
- Idle mechanics requiring offline progress calculation
- Progressive complexity from simple to deep systems

---

## Recommended Architecture: Offline-First PWA

### Phase 1: Offline-First (Launch)
```
Frontend:      SvelteKit + TypeScript
Storage:       IndexedDB (via Dexie.js)
Styling:       Tailwind CSS
Build/Deploy:  Vercel (or GitHub Pages)
Python Tools:  Simulation scripts, data generators
```

### Phase 2: Online Features (Future)
```
Backend:       FastAPI + PostgreSQL
Auth:          Supabase Auth or Firebase Auth
Hosting:       Railway.app or Fly.io
Sync:          IndexedDB ↔ PostgreSQL sync layer
```

---

## Stack Components

### Version Control: **GitHub**

**Choice:** GitHub  
**Why:**
- Dominant platform in 2025 with largest ecosystem
- GitHub Actions for CI/CD (free for public repos)
- GitHub Pages for free static hosting
- Best community support and third-party integrations
- No compelling reason to use GitLab or Bitbucket for this project

**Alternatives Considered:**
- **GitLab:** Better if self-hosting or need integrated DevOps platform
- **Bitbucket:** Better if already using Atlassian ecosystem (Jira, Trello)

---

### Frontend Framework: **Svelte (SvelteKit)**

**Choice:** SvelteKit + TypeScript  
**Why:**
- **Smallest bundle size** - critical for offline PWA performance
- **Best performance** - compiles to vanilla JS, no virtual DOM overhead
- **Less boilerplate** - faster development than React
- **Built-in reactivity** - perfect for game state management
- **SvelteKit** - excellent PWA support, routing, SSG capabilities
- **Modern tooling** - Vite-based, fast dev experience

**Alternatives Considered:**
- **React:** Larger ecosystem, more resources, but heavier bundle and more boilerplate
- **Vue:** Middle ground, but no compelling advantage over Svelte for this use case
- **Vanilla JS + Canvas/Phaser:** Maximum control but more manual work, game engine overhead

**Verdict:** Svelte is the right tool for a performant idle game. React would carry unnecessary weight.

---

### State Management: **Svelte Stores (Built-in)**

**Choice:** Svelte's built-in stores  
**Why:**
- Native reactivity system
- No external library needed
- Simple, performant, sufficient for game state
- Writable, readable, derived stores cover all needs

**No need for:**
- Redux (overkill, too much boilerplate)
- Zustand (unnecessary with Svelte's stores)
- MobX (Svelte already reactive)

---

### Data Persistence: **IndexedDB (via Dexie.js)**

**Choice:** IndexedDB with Dexie.js wrapper  
**Why:**
- **Unlimited storage** (with user permission) - critical for card collections
- **Fully offline** - no server required
- **Structured queries** - perfect for filtering/sorting cards
- **Async API** - non-blocking, won't freeze UI
- **Dexie.js** - makes IndexedDB actually pleasant to use, SQL-like queries
- **Schema versioning** - built-in migration support for game updates

**Why NOT LocalStorage:**
- ❌ 5-10MB limit (too small for card game)
- ❌ Synchronous API (blocks UI)
- ❌ String-only storage (constant JSON parse/stringify)

**Example Data Structure:**
```typescript
// Dexie schema
db.version(1).stores({
  cards: '++id, name, tier, rarity, level',
  decks: '++id, name, tier, active',
  playerState: 'key',
  currencies: 'type, amount'
});
```

---

### Styling: **Tailwind CSS**

**Choice:** Tailwind CSS  
**Why:**
- **Utility-first** - perfect for abstract game UI (shapes, colors, layouts)
- **Tiny production bundle** - only includes used classes
- **Rapid prototyping** - build UI quickly during design iterations
- **Theming** - easy to implement tier color schemes
- **Responsive** - built-in responsive design utilities

**Alternatives Considered:**
- **CSS Modules:** More boilerplate, less rapid iteration
- **Styled Components:** Runtime overhead, not needed with Tailwind
- **Plain CSS:** More manual work, harder to maintain consistency

---

### Build & Development: **Vite**

**Choice:** Vite (via SvelteKit)  
**Why:**
- Built into SvelteKit
- Lightning-fast dev server with HMR
- Optimized production builds
- ES modules-based (modern, fast)

---

### Hosting: **Vercel** (Free Tier)

**Choice:** Vercel  
**Why:**
- **Best developer experience** in 2025
- **Instant deployments** from Git pushes
- **Generous free tier** - more than sufficient for indie game
- **Built-in PWA support** - automatic service worker optimization
- **Global CDN** - fast load times worldwide
- **Preview deployments** - every PR gets a preview URL

**Alternatives Considered:**
- **Netlify:** Similar but slightly less modern DX
- **GitHub Pages:** Free but lacks advanced features (serverless functions, etc.)
- **Cloudflare Pages:** Good but Vercel has better SvelteKit integration

**Cost:** Free for personal projects (generous limits)

---

### Python Usage: **Tooling & Simulation Only**

**Choice:** Python for offline tools, NOT for web server (yet)  
**Why:**
- **Plays to strengths** - you're a pro Python dev
- **Right tool for job** - spreadsheets, simulations, data generation
- **Not for web serving** - JavaScript owns the web frontend

**Python Use Cases:**
1. **Session 1-8 Deliverables:**
   - Balance spreadsheets (resource generation calculators)
   - Combat simulation models
   - Card stat generators
   - Economy modeling tools
   - Progression curve calculators

2. **Build Scripts:**
   - Export card database to JSON
   - Generate TypeScript types from data schemas
   - Validate game data (check for broken card references)
   - Asset pipeline automation

3. **Testing:**
   - Unit tests for game logic (before porting to TS)
   - Simulation validation
   - Balance testing scripts

**Data Flow:**
```
Python (simulation/balance) → JSON exports → TypeScript (game logic)
```

---

### Future Backend: **FastAPI** (When Needed)

**Choice:** FastAPI + PostgreSQL  
**When:** Only when adding online features (leaderboards, sync, multiplayer)  
**Why:**
- **High performance** - async by default, fast as Node.js
- **Modern Python** - type hints, automatic validation
- **Auto-generated docs** - Swagger/OpenAPI UI included
- **Perfect for APIs** - exactly what you need for game backend
- **WebSocket support** - for future real-time features
- **You already know Python** - leverage existing expertise

**Why NOT:**
- **Django:** Overkill (admin panels, templates not needed), not async-first
- **Flask:** Dated (no native async), less modern than FastAPI
- **Node.js/Express:** No advantage, you're stronger in Python

**Hosting for Backend:**
1. **Railway.app** (~$5/month): Best DX, generous free trial, auto-scaling
2. **Fly.io** (~$5-15/month): More control, excellent performance, edge deployment
3. **Render:** Good free tier but slower cold starts

**Don't use Heroku:** Eliminated free tier, expensive for value in 2025

---

### Future Authentication: **Supabase Auth or Firebase Auth**

**Choice:** Supabase Auth (when online features added)  
**Why:**
- **Open source** - can self-host if needed
- **PostgreSQL-based** - same DB as your game data
- **Built-in auth providers** (email, Google, GitHub, etc.)
- **Row-level security** - protect user data at DB level
- **Free tier** - sufficient for indie game
- **Real-time subscriptions** - for sync features

**Alternative:**
- **Firebase Auth:** More mature, larger ecosystem, but vendor lock-in

---

## Development Workflow

### Local Development
```bash
# Frontend development
cd frontend
npm run dev          # Vite dev server on localhost:5173

# Python tools/scripts
cd tools
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python simulate_combat.py
```

### CI/CD Pipeline (GitHub Actions)
```yaml
# .github/workflows/deploy.yml
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - Checkout code
      - Build frontend
      - Run tests
      - Deploy to Vercel
```

### Deployment
- **Automatic:** Push to `main` branch → Vercel auto-deploys
- **Preview:** Open PR → Vercel creates preview URL
- **Rollback:** One-click rollback in Vercel dashboard

---

## Progressive Web App (PWA) Features

### Offline Capabilities
- **Service Worker:** Cache all assets for offline use
- **IndexedDB:** Store game state locally
- **Background Sync:** Queue online actions for when connection returns
- **Offline calculation:** Calculate idle gains since last session locally

### PWA Manifest
```json
{
  "name": "Idle Deck Builder",
  "short_name": "Idle Deck",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#6366f1",
  "background_color": "#ffffff",
  "icons": [...]
}
```

### Installation
- Users can "Add to Home Screen" on mobile
- Desktop PWA installation on Chrome/Edge
- Works like native app after installation

---

## Data Flow Architecture

### Phase 1: Offline-Only
```
User Interaction
    ↓
Svelte Components (UI)
    ↓
Svelte Stores (State)
    ↓
IndexedDB (Persistence)
    ↓
Service Worker (Offline Cache)
```

### Phase 2: Offline + Online Sync
```
User Interaction
    ↓
Svelte Components
    ↓
Svelte Stores (State)
    ↓           ↓
IndexedDB  →  Sync Layer  ←→  FastAPI Backend
(Local)                         ↓
                         PostgreSQL (Server)
```

**Sync Strategy:**
- Local-first: all actions work offline
- Queue online actions when offline
- Sync to server when connection available
- Conflict resolution: server wins for competitive features, local wins for single-player

---

## TypeScript Usage

### Benefits
- **Type safety** - catch bugs at compile time
- **Better IDE support** - autocomplete, refactoring
- **Self-documenting** - types serve as inline documentation
- **Refactoring confidence** - rename/restructure safely

### Example Type Definitions
```typescript
// types/cards.ts
export enum Tier {
  Arcane = 'arcane',
  Fire = 'fire',
  Water = 'water',
  Earth = 'earth',
  Air = 'air'
}

export enum Rarity {
  Common = 'common',
  Rare = 'rare',
  Epic = 'epic',
  Legendary = 'legendary'
}

export interface Card {
  id: string;
  name: string;
  tier: Tier;
  rarity: Rarity;
  attack: number;
  defense: number;
  essenceGeneration?: {
    type: Tier;
    amount: number;
  };
  level: number;
  abilities: CardAbility[];
}

export interface Deck {
  id: string;
  name: string;
  tier: Tier;
  cards: string[]; // Card IDs
  active: boolean;
}
```

---

## Migration Path: Offline → Online

### Step 1: Offline MVP (Launch)
- Build complete game with IndexedDB
- All features work offline
- Deploy as PWA on Vercel
- No backend required

### Step 2: Add Backend (Future)
1. **Set up FastAPI backend** (Railway/Fly.io)
2. **Replicate IndexedDB schema in PostgreSQL**
3. **Add authentication** (Supabase Auth)
4. **Build sync layer:**
   - Export local data to server
   - Import server data to local
   - Handle conflicts

### Step 3: Online Features
- Leaderboards (read from server DB)
- Cloud saves (sync deck/progress)
- Daily challenges (server-side events)
- Multiplayer (WebSocket via FastAPI)

**Key:** Game always works offline, online features are additive.

---

## Alternative Stacks Considered (and Rejected)

### Pure Python Stack (PyScript, Pyodide, Flet)
**Rejected because:**
- ❌ Much larger bundle sizes (Python runtime in browser)
- ❌ Slower performance (WASM overhead)
- ❌ Less mature tooling for web games
- ❌ Smaller ecosystem for UI components
- 🎯 **Wrong tool for the job** - JavaScript owns web frontend

### React Instead of Svelte
**Not rejected, but:**
- ✅ Larger ecosystem, more resources
- ❌ Larger bundle size (~45KB vs ~10KB)
- ❌ More boilerplate (hooks, context, etc.)
- ❌ No performance advantage for this use case
- 🎯 **Svelte is better fit** for performant idle game

### Firebase Instead of FastAPI
**Rejected for primary backend because:**
- ❌ Vendor lock-in (can't self-host)
- ❌ NoSQL limits complex queries (card filtering/sorting)
- ❌ Cost scaling less predictable
- ✅ **Good for auth only** - use Supabase Auth instead

---

## Bundle Size Targets

### Initial Load (PWA)
- **Target:** < 200KB gzipped
- **Breakdown:**
  - Svelte runtime: ~10KB
  - SvelteKit core: ~20KB
  - Dexie.js: ~25KB
  - Tailwind CSS (purged): ~10KB
  - Game logic: ~50KB
  - Assets (initial): ~85KB

### After Code Splitting
- **Core game:** 200KB (loads immediately)
- **Advanced features:** 50KB (lazy loaded)
- **Card assets:** Load on-demand, cached by service worker

### IndexedDB Storage
- **Initial:** ~1MB (starter cards, game logic)
- **Expected growth:** 5-20MB (full collection)
- **Maximum:** Unlimited with user permission

---

## Performance Targets

### Metrics
- **First Contentful Paint:** < 1.5s
- **Time to Interactive:** < 3s
- **Lighthouse Score:** 95+ (Performance, PWA)
- **Frame Rate:** 60fps during animations
- **IndexedDB Query:** < 50ms for card filtering

### Optimization Strategies
- Code splitting (lazy load non-critical features)
- Asset lazy loading (load card images on-demand)
- Service Worker caching (instant repeat visits)
- Svelte's compile-time optimizations
- Minimal JavaScript runtime

---

## Security Considerations

### Offline Version (Phase 1)
- **No server = no attack surface**
- **Client-side only** - cheating possible but acceptable for single-player
- **No sensitive data** - game state only
- **HTTPS via Vercel** - secure even if no backend

### Online Version (Phase 2)
- **Server validation** - never trust client
- **Authentication** - secure user accounts (Supabase/Firebase)
- **Rate limiting** - prevent API abuse (FastAPI middleware)
- **Row-level security** - PostgreSQL RLS (Supabase)
- **CORS configuration** - restrict API access
- **Input validation** - Pydantic models (FastAPI)

---

## Testing Strategy

### Frontend Testing
- **Unit Tests:** Vitest (Vite's test runner)
- **Component Tests:** Svelte Testing Library
- **E2E Tests:** Playwright (optional, for critical paths)

### Backend Testing (Future)
- **API Tests:** pytest + httpx (FastAPI testing)
- **Database Tests:** pytest fixtures with test DB

### Python Tools Testing
- **Unit Tests:** pytest for simulation scripts
- **Validation:** Test card generation, balance calculations

---

## Learning Resources

### SvelteKit + TypeScript
- **Official Tutorial:** https://learn.svelte.dev/
- **SvelteKit Docs:** https://kit.svelte.dev/docs
- **TypeScript Handbook:** https://www.typescriptlang.org/docs/

### Dexie.js (IndexedDB)
- **Official Docs:** https://dexie.org/docs/
- **Tutorial:** https://dexie.org/docs/Tutorial/

### Tailwind CSS
- **Official Docs:** https://tailwindcss.com/docs
- **Playground:** https://play.tailwindcss.com/

### FastAPI (Future)
- **Official Tutorial:** https://fastapi.tiangolo.com/tutorial/
- **Real Python Course:** Modern Python web development

### PWA Development
- **MDN Guide:** Progressive Web Apps
- **Google's PWA Training:** web.dev/progressive-web-apps/

---

## Cost Breakdown

### Phase 1: Offline Version
- **Vercel:** Free (generous limits)
- **GitHub:** Free (public repo)
- **Domain (optional):** $12/year (Namecheap, Cloudflare)
- **Total:** $0-12/year

### Phase 2: Online Features
- **Vercel:** Still free (frontend)
- **Railway/Fly.io:** $5-15/month (backend)
- **Supabase:** Free tier (up to 500MB DB, 2GB bandwidth)
- **Domain:** $12/year
- **Total:** $60-192/year

### Scaling (1000+ active users)
- **Vercel:** Still free (hobby tier)
- **Backend hosting:** $20-50/month
- **Database:** $10-25/month (Supabase Pro)
- **Total:** $30-75/month (~$360-900/year)

---

## Decision Timeline

### Immediate (Now)
- ✅ Document tech stack options (this document)
- ⏳ Finalize after Session 1-2 design work

### Session 1-2 (Design Phase)
- Use Python for simulation/spreadsheets
- No frontend development yet
- Validate tech choices against concrete examples

### Session 3-4 (Validation)
- **Build spike/prototype** with SvelteKit + IndexedDB
- Test performance with sample cards
- Validate data model with real game logic

### Session 5+ (Development)
- Full implementation if spike successful
- Iterate on tech choices if needed
- Document any deviations from this plan

---

## Open Questions

1. **Game title?** Affects domain, branding, metadata
2. **Desktop app?** (Tauri could package PWA as native app)
3. **Mobile native?** (Capacitor could build iOS/Android from PWA)
4. **Monetization?** (Affects online features priority)

---

## Verdict

**Recommended Stack:**
```
Version Control:  GitHub
Frontend:         SvelteKit + TypeScript
State:            Svelte stores
Storage:          IndexedDB (Dexie.js)
Styling:          Tailwind CSS
Hosting:          Vercel (free)
Python:           Tooling/simulation only

Future Backend:   FastAPI + PostgreSQL
Future Hosting:   Railway.app or Fly.io
Future Auth:      Supabase Auth
```

**Confidence Level:** High - this is the right tool for the job given your requirements and constraints.

**Risk Level:** Low - all technologies are mature, well-documented, and proven in production.

**Next Step:** Follow git setup instructions, initialize project, revisit after Session 1-2 to validate with concrete examples.

---

**Document Status:** Complete - Ready for validation in Session 3+  
**Last Updated:** 2025-11-04  
**Author:** Design/AI Partnership

