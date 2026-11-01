# Workflow: designing an app the Apple way, step by step

This is the procedure an agent follows to turn a product idea into screens, components, and code that conform to the
Human Interface Guidelines. Each step names the guide or reference to read and the artifact to produce. Do the steps in
order; later steps assume the earlier decisions are written down.

## Step 0. Capture the brief

Write a short design brief before touching UI:

- What the app is for, in one sentence (Purpose principle: make something meaningful).
- The three to five tasks people do most often (Simplicity: include just what is necessary).
- Target platforms and whether they share one codebase (SwiftUI, UIKit, AppKit, web). Each platform must still feel native (Flexibility: approach every platform with intention).
- The emotion the app should evoke (Delight: identify the emotion you want to inspire).
- Constraints: offline, accounts, payments, sensitive data, media playback, games.

Read: [Design principles](../references/getting-started/design-principles.md).

## Step 1. Learn the platform

For each target platform read the matching "Designing for" page and write down its traits, inputs, system features, and best practices. The summary is in [platforms.md](platforms.md).

Decisions to record:
- Primary input (touch, pointer and keyboard, remote, eyes and hands, Digital Crown) and the resulting minimum control size and spacing.
- Viewing distance and the resulting default type size.
- Session length and interruption model (glanceable watch, deep-focus Mac, shared living-room TV).
- System experiences to plan for from the start: widgets, Live Activities, complications, Siri and App Shortcuts, Spotlight, notifications, menu bar, Dock menu, Top Shelf, Control Center controls.

## Step 2. Define the information architecture

1. List every content type and the actions on it.
2. Group into three to five top-level areas at most. If you need more, you have a sidebar app or need to rethink.
3. Order areas and items by frequency and importance (Layout: order by relative importance; Menus: important items first).
4. Decide the hierarchy depth. Two levels fit a sidebar; deeper hierarchies need a split view with a content list between sidebar and detail.
5. Write the names. Single words for tabs, short noun phrases for section headers, verbs for actions, title-style capitalization for labels, no articles.

Artifact: a tree of areas, screens, and actions with their labels.

## Step 3. Choose the navigation model

Use this decision table (details and platform notes in [components.md](components.md)):

| Situation | iOS | iPadOS | macOS | tvOS | visionOS | watchOS |
|---|---|---|---|---|---|---|
| Few top-level sections (2 to 5) | Tab bar at bottom (Liquid Glass, optional search tab) | Tab bar at top, optionally convertible to sidebar (sidebarAdaptable) | Sidebar in a split view, or a toolbar-level segmented control for small apps | Tab bar at top (68 pt) | Vertical tab bar on the leading side | Vertical tab view with page controls, or a list |
| Many sections or user-defined collections | Tab bar first; move extras into a More tab only if unavoidable | Tab bar convertible to sidebar; let people customize | Sidebar with disclosure groups, at most two levels | Split view for filtering | Tab bar plus a sidebar inside a tab for deep hierarchies | Short list; avoid deep hierarchies |
| Hierarchical content (list to detail) | Navigation stack inside a tab; large title that collapses on scroll; standard Back button | Two or three column split view (NavigationSplitView) | Split view with sidebar, content list, detail | Split view (one third / two thirds) | Split view instead of new windows | List then detail; detail pages in a vertical tab view |
| Documents or multiple contexts | One window | Multiple resizable windows, window controls on the leading edge of the toolbar | Multiple windows, document menu in the toolbar, full menu bar | Single screen | Windows and volumes with min and max sizes | Single screen |
| Frequent commands on the current view | Toolbar (top or bottom), More menu for overflow | Toolbar, customizable; can share the top row with a tab bar | Toolbar in the window frame, every item also in the menu bar | Focus-driven buttons | Toolbar at the bottom edge of the window; ornaments for window-related controls | Toolbar buttons in corners or a scrolling toolbar button |

Rules that always apply:
- Tab bars navigate; they never hold actions. Never hide or disable tabs. Keep the tab bar visible except under a modal.
- Toolbar: at most three groups, one prominent primary action on the trailing edge (Done, Submit), standard Back and Close symbols with no text labels, title under 15 characters, never the app name.
- Switch tab bar to sidebar when width grows; never change what the app can do based on size.
- Keep groupings and placements consistent across platforms.

Artifact: a navigation map per platform (what container holds what, and how people move between levels).

## Step 4. Inventory the screens and pick the presentation for each

For every screen decide whether it is a destination in the hierarchy or a presentation on top of it. Use the presentation decision tree:

- Critical, unexpected information that needs a decision now: **Alert**. Two buttons ideally, default on the trailing side or top, Cancel on the leading side or bottom, destructive style when the person did not choose the destructive action, never just "OK" unless purely informational, never at launch, never for undoable common actions.
- Choices that follow an action the person just took (for example canceling a draft): **Action sheet** (iOS, iPadOS, watchOS; a confirmation dialog in SwiftUI). Short title, destructive options at the top, Cancel at the bottom, no scrolling.
- A scoped task with its own content that returns to the parent when done: **Sheet**. Cancel on the leading edge, Done on the trailing edge (iOS and iPadOS), medium and large detents with a grabber on iPhone, one sheet at a time, always pair Done with Cancel or Back, swipe to dismiss with confirmation if there are unsaved changes.
- A small amount of related information or a few controls anchored to a control: **Popover** (regular width only; use a sheet in compact width). Saves on dismiss, one at a time, nothing on top except an alert, not for warnings.
- Immersive or multistep editing, media, camera: **Full-screen modal**. Clear way out, confirmation before data loss.
- macOS repeated input while observing results (find and replace, inspectors, tools): **Panel**; supplementary controls that float.
- Everything else is a pushed or selected destination, not a modal.

Modality rules: modal only when there is a clear benefit, short and simple, one path through, obvious dismissal, title that names the task, one modal at a time, confirm before discarding user content.

Artifact: a screen list with, for each screen, its container (tab, sidebar section, stack level), its presentation type, its title, and its primary action.

## Step 5. Compose each screen from system components

For each screen, list the content and controls, then map each to a component using the "Choosing a component" table in [components.md](components.md). Apply these composition rules:

- Reading order: most important content top and leading; group related items with space, containers, or separators; progressive disclosure for secondary detail.
- Lists and tables for text; collections for visually dominant or variably sized items; outline views (macOS) for hierarchical data.
- Controls: segmented control for 2 to 5 closely related mutually exclusive choices that affect a view; pop-up button for a flat list of mutually exclusive options; pull-down button for commands related to its label; toggle (switch style only in list rows) for on/off; picker for medium to long ordered value lists; slider for a continuous range (never for volume); stepper for small incremental changes; text field for short specific text with hint text; text view for long or formatted text.
- Status: determinate progress indicator whenever you can estimate; indeterminate only when you cannot (never on watchOS); activity indicator inside a button for actions that do not complete instantly (iOS, iPadOS).
- One or two prominent (accent) buttons per view; style, not size, distinguishes the preferred action; every custom button has a press state; 44x44 pt hit regions (60 pt visionOS).
- Context menus for item-specific actions that are also available elsewhere; menus with icons for the most common actions only, all or none per group, separators between groups, submenus one level deep.
- Search: one clearly identified location; placeholder text that states the scope; results as you type; suggestions and recent searches (mind privacy); scope bar or tokens to narrow; bottom placement on iPhone when there is room, trailing toolbar on iPad and Mac, dedicated search tab for discovery.
- Empty states tell people what to do next.

Artifact: for each screen, an ordered list of components with their labels, states, and the API (SwiftUI, UIKit, AppKit) or web element you will use.

## Step 6. Define the visual system

Fill in the tokens from [design-tokens.md](design-tokens.md); do not invent values.

1. Typography: system text styles only (Large Title, Title 1 to 3, Headline, Body, Callout, Subhead, Footnote, Caption 1 and 2); custom font only for headlines and only if it supports Dynamic Type and Bold Text. Body 17 pt iOS, 13 pt macOS, 29 pt tvOS, 16 pt watchOS. Never below the minimums.
2. Color: semantic system colors for text, backgrounds, separators, fills; one accent color for primary actions and selection; system colors (red, orange, yellow, green, mint, teal, cyan, blue, indigo, purple, pink, brown) for status and categories; every custom color with light, dark, and increased-contrast variants; contrast 4.5:1 minimum, 7:1 goal.
3. Materials: Liquid Glass only for bars, sidebars, popovers, alerts (regular variant), clear variant only over media; standard materials for grouping in the content layer; scroll edge effects instead of solid bar backgrounds; content extends under bars.
4. Shape: use system component shapes; custom components in bars use corner radii concentric with the bar; visionOS prefers circles and capsules.
5. Iconography: SF Symbols with weight matched to text; outline in bars and lists, fill in iOS tab bars; the standard symbols for standard actions; custom symbols built from templates.
6. Motion: system transitions; purposeful, brief, cancelable custom animation; Reduce Motion alternatives; animated symbols for state changes.
7. Dark Mode and Increase Contrast: verify every screen in both appearances with both settings.

Artifact: a token sheet (styles, colors, materials, symbols) referenced by every screen spec.

## Step 7. Write the words

Follow [Writing](../references/foundations/writing.md) and the Content sections of each component page:

- Voice and tone decided once; terms list kept.
- Buttons and menu items: verbs, title case, no articles, ellipsis when more input follows.
- Alerts: title describes what happened and why; message only if it adds value, sentence case; button titles that state the result ("Delete Draft", "Keep Editing"), "Cancel" exactly for cancel.
- Text fields: visible labels plus hint text showing the format; inline errors next to the field that say how to fix the problem.
- Settings labels describe the on state; link directly to settings.
- Notifications: concise, no marketing in Time Sensitive, never an error message, never "open the app to...".
- Permission purpose strings: one clear sentence about how the data is used.
- Empty states, onboarding tips, and help: inclusive, device-appropriate verbs (tap vs click), no "we", no "the user".

Artifact: a copy deck keyed by screen and component.

## Step 8. Design the system moments

Plan these flows explicitly; the patterns guide ([patterns.md](patterns.md)) has the rules.

- Launch: instant, launch screen identical to the first screen with no text or logo, restore previous state, no splash screen unless part of onboarding.
- Onboarding: optional, interactive, short, context-specific tips preferred, no licensing, no large downloads, permissions only when needed.
- Accounts: delay sign-in as long as possible, Sign in with Apple or passkeys, explain the benefit of an account, allow deletion.
- Permissions: just in time, system prompt, honest purpose string, one-button pre-alert at most.
- Loading: show something immediately, let people keep working, determinate progress when possible, educational or entertaining content for long waits.
- Feedback: inline status first, alerts for critical actionable issues, confirmation only for significant completions, warnings only for unexpected irreversible loss, explain why a command cannot run.
- Undo and redo everywhere content changes; drag and drop with alternatives.
- Settings: good defaults, minimal count, in the system Settings app or an in-app Settings area as the platform expects, never duplicating system settings.
- Notifications, widgets, Live Activities, complications, App Shortcuts, Spotlight: high value, glanceable, never promotional.
- Ratings: only after demonstrated engagement, never interrupting, system prompt only.
- Multitasking: pause what needs attention, handle audio interruptions, finish user-initiated work in the background.

## Step 9. Platform adaptation pass

For each additional platform, re-run steps 3 to 6 against that platform's column in [platforms.md](platforms.md). Typical changes:

- iPhone to iPad: tab bar moves to the top and may convert to a sidebar; split views replace stacks; popovers replace sheets in regular width; windows resize and gain window controls; keyboard shortcuts and pointer effects appear; menu bar on iPad.
- iPad to Mac: menu bar with the standard menus and every toolbar command, window states (main, key, inactive), panels, Dock menu, keyboard-first interaction, 13 pt body, 28 pt controls, no Dynamic Type, alternating row colors and sortable columns in tables, the person's accent color may override yours.
- To tvOS: focus-based navigation with scaling feedback, 60/80 pt safe areas, 29 pt body, remote and controller input, Top Shelf.
- To visionOS: windows with glass, vertical tab bar, bottom toolbar, ornaments, 60 pt targets and spacing, eye and hand input, sound feedback instead of haptics, comfort rules.
- To watchOS: glanceable screens, Digital Crown scrolling, full-width capsule buttons, complications and notifications as primary surfaces, no indeterminate spinners.
- To web: see [web.md](web.md).

## Step 10. Review before shipping

Run the checklist in SKILL.md and the detailed accessibility list in [foundations.md](foundations.md). Then verify on device or simulator at the smallest and largest layouts, the largest Dynamic Type size, Dark Mode with Increase Contrast and Reduce Transparency, right-to-left locale, VoiceOver, and keyboard-only (Full Keyboard Access).

## Design spec template

Use this skeleton for the deliverable; one file per app or per platform.

```
# <App> design spec (<platform>)

## Brief
Purpose: ...
Core tasks: 1. ... 2. ... 3. ...
Emotion: ...

## Information architecture
- Area (tab/sidebar item, symbol name)
  - Screen (container, presentation, title, primary action)

## Navigation
Container: ... (why)
Hierarchy: ...

## Screens
### <Screen title>
Purpose: ...
Layout (reading order): ...
Components: | element | component | label | state(s) | API |
Presentation: ...
Empty / loading / error states: ...
Accessibility: labels, Dynamic Type behavior, alternatives to gestures

## Visual system
Text styles used: ...
Colors: accent, semantic roles, status colors
Materials: ...
Symbols: ...
Motion: ...

## Copy deck
| screen | element | text | notes |

## System moments
Launch, onboarding, permissions, accounts, notifications, widgets, settings

## Review results
Checklist items with pass/fail and fixes
```
