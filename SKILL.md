---
name: apple-design
description: Design and build apps the way Apple does, following the official Human Interface Guidelines (HIG) for iOS, iPadOS, macOS, tvOS, visionOS, and watchOS, with a translation for web apps. Use whenever work touches app UI or UX on any platform - planning an app's structure and navigation, choosing and styling components (tab bars, sidebars, toolbars, buttons, sheets, alerts, menus, lists, forms, widgets), layout and safe areas, typography and Dynamic Type, color and Dark Mode, Liquid Glass materials, app icons and SF Symbols, accessibility, UI copy, onboarding, permissions, notifications, gestures and keyboard shortcuts, or Apple technologies (Apple Pay, Sign in with Apple, Siri, CarPlay, HealthKit). Also use to review SwiftUI, UIKit, AppKit, or web interfaces against Apple's guidance, or to answer "what does Apple recommend" questions. Contains every HIG page (173) as local Markdown plus step-by-step workflow, design tokens, and component decision guides.
---

# Apple Design (Human Interface Guidelines)

This skill turns Apple's Human Interface Guidelines into a working procedure for an AI coding agent. It contains:

| Part | Purpose |
|---|---|
| `guides/workflow.md` | The step-by-step process: brief, platform, information architecture, navigation, screens, components, visual system, copy, system moments, platform adaptation, review. Includes a design spec template. |
| `guides/design-tokens.md` | Every number: control sizes, spacing, type scales per platform, system colors (hex), semantic colors, contrast, materials, icon specs, gestures, shortcuts. |
| `guides/components.md` | Decision table plus an entry for every HIG component: when to use, what to use instead, rules, platform notes, APIs, web equivalent. |
| `guides/patterns.md` | Every HIG pattern (launching, onboarding, modality, feedback, searching, settings, notifications, and so on) and every input, with rules and web translations. |
| `guides/technologies.md` | Every Apple technology page (Apple Pay, Sign in with Apple, Siri, CarPlay, HealthKit, and so on) with required wording and rules. |
| `guides/foundations.md` | Condensed rules from all eighteen Foundations pages (accessibility, color, typography, layout, materials, icons, writing, privacy...). |
| `guides/platforms.md` | What changes per platform: iOS, iPadOS, macOS, tvOS, visionOS, watchOS, iPhone Duo, games. Menu bar anatomy, window states, focus, spatial rules. |
| `guides/web.md` | How to apply all of the above to a web app: CSS tokens, breakpoints mapped from size classes, materials, component-to-HTML/ARIA mapping, keyboard, accessibility. Clearly marked as a translation. |
| `references/` | All 173 HIG pages as faithful Markdown, in Apple's section hierarchy, each with its source URL. `INDEX.md` lists them with summaries. |

## How to work

1. **Start from the workflow.** Read `guides/workflow.md` and follow its steps in order. Write the brief and the information architecture before drawing or coding any screen.
2. **Decide with the decision tables.** Navigation model: workflow Step 3. Presentation (alert, action sheet, sheet, popover, full screen, panel): workflow Step 4. Component choice: the table at the top of `guides/components.md`. Pattern for a moment in the app (first launch, sign-in, permission, error, empty state...): the table at the top of `guides/patterns.md`.
3. **Take every value from the tokens.** Sizes, type, colors, spacing, and icon specs come from `guides/design-tokens.md`. If a number is not there and not in a reference page, say so and mark the value as a convention rather than presenting it as Apple's guidance.
4. **Read the reference page before implementing a component or pattern.** The guides summarize; the reference page under `references/` has the full text, platform considerations, and developer API links. Cite the page (its `Source:` URL) in specs and reviews.
5. **Adapt per platform, do not port.** After the first platform, re-run workflow Steps 3 to 6 against `guides/platforms.md` for each additional platform, and `guides/web.md` for the web.
6. **Review with the checklist below** and fix everything that fails before calling the work done.

Search tips: every best practice in the references is a bold sentence that starts a paragraph, so `grep -rn '^\*\*' references/components/presentation` lists all presentation rules; `grep -rli 'liquid glass' references` finds every page on a topic.

## The eight design principles

Apple grounds the whole HIG in these (full text: `references/getting-started/design-principles.md`). Weigh every decision against them.

| Principle | Rule | Apply it by |
|---|---|---|
| Purpose | Make something meaningful. | Keep the three to five core tasks great; cut the rest. |
| Agency | Let people do things their own way. | Stay out of the way, allow exploration, make every mistake recoverable (undo, confirmation only for unexpected loss). |
| Responsibility | Act in people's best interest. | Ask for data only when needed, explain why, process on device, protect it. |
| Familiarity | Build on what people know. | System components, standard placements and symbols, consistent behavior, clear feedback. |
| Flexibility | Adapt to diverse contexts and needs. | Size classes, Dynamic Type, every input method, accessibility from the start, each platform with intention. |
| Simplicity | Be clear and direct. | Only what is necessary, concise words, visible hierarchy. |
| Craft | Care about every detail. | Prototype, iterate, test on devices, keep the bar high after shipping. |
| Delight | Make it human. | Choose the emotion, create defining moments, never confuse delight with decoration. |

## Non-negotiable rules

These recur throughout the guidelines. Violating one is a defect.

Structure
- System components and standard behaviors first; custom only when there is a clear benefit, and then matching system look and behavior.
- Layout from size classes and safe areas, never from device type or orientation; functionality never changes with size.
- Tab bars navigate (3 to 5 tabs, never hidden or disabled, never actions). Toolbars act (at most three groups, one prominent primary action trailing, standard Back and Close symbols, title under 15 characters, never the app name). Sidebars show at most two levels.
- Modality only with a clear benefit, one modal at a time, obvious dismissal, confirmation before discarding user content. Alerts only for critical actionable information, never on launch, never for undoable actions, never plain "OK" unless informational. Action sheets for choices after an action. Popovers only in regular width.

Visual
- System text styles with Dynamic Type; body 17 pt iOS/iPadOS/visionOS, 13 pt macOS, 29 pt tvOS, 16 pt watchOS; never below 11/10/23/12/12 pt; avoid light weights.
- Semantic system colors; one accent used sparingly; custom colors with light, dark, and increased-contrast variants; contrast 4.5:1 minimum, 7:1 goal; never color alone.
- Both appearances always; no in-app appearance switch.
- Liquid Glass only in the floating controls layer, regular variant by default, clear only over media with 35 percent dimming when bright; standard materials in content; no solid bar backgrounds; content extends under bars.
- Hit regions 44x44 pt (60 pt visionOS, 28 pt macOS default), about 12 pt between bezeled controls, 24 pt between plain ones; a press state on every custom button; one or two prominent buttons per view.
- SF Symbols for interface icons with weight matched to text; standard symbols for standard actions; layered app icon with default, dark, clear, and tinted appearances; nothing baked in; no Apple hardware or trademarks.
- Motion purposeful, brief, cancelable, and optional.

Behavior and words
- Launch instantly, launch screen identical to the first screen with no text or logo, restore state, no splash screen except inside onboarding.
- Onboarding optional and interactive; sign-in delayed as long as possible; Sign in with Apple or passkeys; permissions requested just in time with an honest purpose string and the system prompt.
- Accessibility: VoiceOver labels, keyboard and Switch Control, captions, alternatives to every gesture, no timed UI, Reduce Motion and Reduce Transparency honored, text enlargement to 200 percent.
- Copy: verbs on buttons, title case for buttons and menu items, sentence case for messages, hint text in fields, errors beside the field that say how to fix them, no "we", no "the user", tap on touch and click with a pointer.
- Notifications, widgets, Live Activities, complications, and Top Shelf carry high-value information, never ads or marketing; ratings requested only after engagement via the system prompt.

## Platform snapshot

Full detail in `guides/platforms.md`.

| Platform | Defining traits | Inputs | Navigation anatomy |
|---|---|---|---|
| iOS | Medium display, held, short frequent sessions | Multi-Touch, virtual keyboard, voice | Bottom tab bar, top toolbar with large title, stacks, sheets |
| iPadOS | Large display, multitasking, resizable windows | Touch, keyboard, trackpad, Apple Pencil | Top tab bar convertible to sidebar, split views, popovers, menu bar |
| macOS | Large displays, many windows, long sessions | Keyboard, pointer, trackpad, touch display | Sidebar split view, toolbar in the frame, full menu bar, panels |
| tvOS | Viewed from 8+ ft, focus-based | Siri Remote, controller, voice | Top tab bar, focus, split views, Top Shelf |
| visionOS | 3D space, windows and volumes, immersion levels | Eyes plus hands | Vertical tab bar, bottom toolbar, ornaments, sheets centered |
| watchOS | Glanceable, sub-minute, Always On | Digital Crown, tap, Action button | Vertical tab views, lists, toolbar corners, complications |
| iPhone Duo | Two displays, folding, vertical bars | Touch | Side-mounted toolbars and tab bars, arrangement views |
| Web (translation) | Any browser | Pointer, touch, keyboard | Size-class breakpoints, native elements, ARIA (see `guides/web.md`) |

## Design review checklist

Run on every screen, mockup, or UI code change. Each item names where the rule lives.

1. System components and standard behaviors used wherever they exist; custom controls match system look and have press, focus, and disabled states. (components.md)
2. Layout from size classes, safe areas, and layout guides; survives the largest Dynamic Type size, the smallest and largest window, and right-to-left. (foundations.md Layout, Right to left)
3. Navigation: correct container for the platform; tabs navigate only; toolbar groups and primary action placed per rules; titles short and meaningful. (workflow Step 3)
4. Presentation: each modal is the right type, dismissible, one at a time, with confirmation before data loss. (workflow Step 4)
5. Controls at least 44x44 pt (60 visionOS, 28 macOS) with adequate spacing. (design-tokens.md)
6. Type: system text styles, no size below the platform minimum, no light weights, hierarchy preserved at large sizes. (design-tokens.md)
7. Color: semantic colors, one accent used sparingly, contrast 4.5:1 or better in light, dark, and Increase Contrast, meaning never carried by color alone. (foundations.md Color, Dark Mode)
8. Materials: Liquid Glass confined to bars, sidebars, popovers, alerts; content extends beneath; no solid bar fills; Reduce Transparency handled. (foundations.md Materials)
9. Icons: SF Symbols with matched weight, standard symbols for standard actions, app icon layered and consistent across platforms with all appearances. (foundations.md Icons, App icons)
10. Accessibility: VoiceOver labels on all images and controls, keyboard-only operation, captions, gesture alternatives, no timed UI, Reduce Motion. (foundations.md Accessibility)
11. Copy: verbs, correct capitalization, hints and inline errors, inclusive language, alert text and buttons per rules. (foundations.md Writing)
12. System moments: instant launch and state restoration, optional onboarding, delayed sign-in, just-in-time permissions, good defaults, minimal settings. (patterns.md)
13. Notifications, widgets, Live Activities, complications, and ratings prompts are high value and non-promotional. (components.md System experiences, patterns.md)
14. Each platform gets its own adaptation pass; nothing is a straight port. (platforms.md)
15. Every claim in the spec cites a HIG page; conventions not from the HIG are labeled as such.

## Page index (all 173 pages)

Each section's `README.md` is Apple's overview page. `INDEX.md` has one-line summaries. `references/README.md` is the HIG home page.

### Getting started ([overview](references/getting-started/README.md))

[Design principles](references/getting-started/design-principles.md), [Designing for iOS](references/getting-started/designing-for-ios.md), [Designing for iPadOS](references/getting-started/designing-for-ipados.md), [Designing for macOS](references/getting-started/designing-for-macos.md), [Designing for tvOS](references/getting-started/designing-for-tvos.md), [Designing for visionOS](references/getting-started/designing-for-visionos.md), [Designing for watchOS](references/getting-started/designing-for-watchos.md), [Designing for games](references/getting-started/designing-for-games.md), [Designing for iPhone Duo](references/getting-started/designing-for-iphone-duo.md)

### Foundations ([overview](references/foundations/README.md))

[Accessibility](references/foundations/accessibility.md), [App icons](references/foundations/app-icons.md), [Branding](references/foundations/branding.md), [Color](references/foundations/color.md), [Dark Mode](references/foundations/dark-mode.md), [Icons](references/foundations/icons.md), [Images](references/foundations/images.md), [Immersive experiences](references/foundations/immersive-experiences.md), [Inclusion](references/foundations/inclusion.md), [Layout](references/foundations/layout.md), [Materials](references/foundations/materials.md), [Motion](references/foundations/motion.md), [Privacy](references/foundations/privacy.md), [Right to left](references/foundations/right-to-left.md), [SF Symbols](references/foundations/sf-symbols.md), [Spatial layout](references/foundations/spatial-layout.md), [Typography](references/foundations/typography.md), [Writing](references/foundations/writing.md)

### Patterns ([overview](references/patterns/README.md))

[Charting data](references/patterns/charting-data.md), [Collaboration and sharing](references/patterns/collaboration-and-sharing.md), [Drag and drop](references/patterns/drag-and-drop.md), [Entering data](references/patterns/entering-data.md), [Feedback](references/patterns/feedback.md), [File management](references/patterns/file-management.md), [Going full screen](references/patterns/going-full-screen.md), [Launching](references/patterns/launching.md), [Live-viewing apps](references/patterns/live-viewing-apps.md), [Loading](references/patterns/loading.md), [Managing accounts](references/patterns/managing-accounts.md), [Managing notifications](references/patterns/managing-notifications.md), [Modality](references/patterns/modality.md), [Multitasking](references/patterns/multitasking.md), [Offering help](references/patterns/offering-help.md), [Onboarding](references/patterns/onboarding.md), [Playing audio](references/patterns/playing-audio.md), [Playing haptics](references/patterns/playing-haptics.md), [Playing video](references/patterns/playing-video.md), [Printing](references/patterns/printing.md), [Ratings and reviews](references/patterns/ratings-and-reviews.md), [Searching](references/patterns/searching.md), [Settings](references/patterns/settings.md), [Undo and redo](references/patterns/undo-and-redo.md), [Workouts](references/patterns/workouts.md)

### Components ([overview](references/components/README.md))



**Content** ([overview](references/components/content/README.md))

[Charts](references/components/content/charts.md), [Image views](references/components/content/image-views.md), [Text views](references/components/content/text-views.md), [Web views](references/components/content/web-views.md)

**Layout and organization** ([overview](references/components/layout-and-organization/README.md))

[Boxes](references/components/layout-and-organization/boxes.md), [Collections](references/components/layout-and-organization/collections.md), [Column views](references/components/layout-and-organization/column-views.md), [Disclosure controls](references/components/layout-and-organization/disclosure-controls.md), [Labels](references/components/layout-and-organization/labels.md), [Lists and tables](references/components/layout-and-organization/lists-and-tables.md), [Lockups](references/components/layout-and-organization/lockups.md), [Outline views](references/components/layout-and-organization/outline-views.md), [Split views](references/components/layout-and-organization/split-views.md), [Tab views](references/components/layout-and-organization/tab-views.md)

**Menus and actions** ([overview](references/components/menus-and-actions/README.md))

[Activity views](references/components/menus-and-actions/activity-views.md), [Buttons](references/components/menus-and-actions/buttons.md), [Context menus](references/components/menus-and-actions/context-menus.md), [Dock menus](references/components/menus-and-actions/dock-menus.md), [Edit menus](references/components/menus-and-actions/edit-menus.md), [Home Screen quick actions](references/components/menus-and-actions/home-screen-quick-actions.md), [Menus](references/components/menus-and-actions/menus.md), [Ornaments](references/components/menus-and-actions/ornaments.md), [Pop-up buttons](references/components/menus-and-actions/pop-up-buttons.md), [Pull-down buttons](references/components/menus-and-actions/pull-down-buttons.md), [The menu bar](references/components/menus-and-actions/the-menu-bar.md), [Toolbars](references/components/menus-and-actions/toolbars.md)

**Navigation and search** ([overview](references/components/navigation-and-search/README.md))

[Path controls](references/components/navigation-and-search/path-controls.md), [Search fields](references/components/navigation-and-search/search-fields.md), [Sidebars](references/components/navigation-and-search/sidebars.md), [Tab bars](references/components/navigation-and-search/tab-bars.md), [Token fields](references/components/navigation-and-search/token-fields.md)

**Presentation** ([overview](references/components/presentation/README.md))

[Action sheets](references/components/presentation/action-sheets.md), [Alerts](references/components/presentation/alerts.md), [Page controls](references/components/presentation/page-controls.md), [Panels](references/components/presentation/panels.md), [Popovers](references/components/presentation/popovers.md), [Scroll views](references/components/presentation/scroll-views.md), [Sheets](references/components/presentation/sheets.md), [Windows](references/components/presentation/windows.md)

**Selection and input** ([overview](references/components/selection-and-input/README.md))

[Color wells](references/components/selection-and-input/color-wells.md), [Combo boxes](references/components/selection-and-input/combo-boxes.md), [Digit entry views](references/components/selection-and-input/digit-entry-views.md), [Image wells](references/components/selection-and-input/image-wells.md), [Pickers](references/components/selection-and-input/pickers.md), [Segmented controls](references/components/selection-and-input/segmented-controls.md), [Sliders](references/components/selection-and-input/sliders.md), [Steppers](references/components/selection-and-input/steppers.md), [Text fields](references/components/selection-and-input/text-fields.md), [Toggles](references/components/selection-and-input/toggles.md), [Virtual keyboards](references/components/selection-and-input/virtual-keyboards.md)

**Status** ([overview](references/components/status/README.md))

[Activity rings](references/components/status/activity-rings.md), [Gauges](references/components/status/gauges.md), [Progress indicators](references/components/status/progress-indicators.md), [Rating indicators](references/components/status/rating-indicators.md)

**System experiences** ([overview](references/components/system-experiences/README.md))

[App Shortcuts](references/components/system-experiences/app-shortcuts.md), [Complications](references/components/system-experiences/complications.md), [Controls](references/components/system-experiences/controls.md), [Live Activities](references/components/system-experiences/live-activities.md), [Notifications](references/components/system-experiences/notifications.md), [Snippets](references/components/system-experiences/snippets.md), [Status bars](references/components/system-experiences/status-bars.md), [Top Shelf](references/components/system-experiences/top-shelf.md), [Watch faces](references/components/system-experiences/watch-faces.md), [Widgets](references/components/system-experiences/widgets.md)

### Inputs ([overview](references/inputs/README.md))

[Action button](references/inputs/action-button.md), [Apple Pencil and Scribble](references/inputs/apple-pencil-and-scribble.md), [Camera Control](references/inputs/camera-control.md), [Digital Crown](references/inputs/digital-crown.md), [Eyes](references/inputs/eyes.md), [Focus and selection](references/inputs/focus-and-selection.md), [Game controls](references/inputs/game-controls.md), [Gestures](references/inputs/gestures.md), [Gyroscope and accelerometer](references/inputs/gyro-and-accelerometer.md), [Keyboards](references/inputs/keyboards.md), [Nearby interactions](references/inputs/nearby-interactions.md), [Pointing devices](references/inputs/pointing-devices.md), [Remotes](references/inputs/remotes.md)

### Technologies ([overview](references/technologies/README.md))

[AirPlay](references/technologies/airplay.md), [Always On](references/technologies/always-on.md), [App Clips](references/technologies/app-clips.md), [Apple In-App Purchase](references/technologies/apple-in-app-purchase.md), [Apple Pay](references/technologies/apple-pay.md), [Augmented reality](references/technologies/augmented-reality.md), [CareKit](references/technologies/carekit.md), [CarPlay](references/technologies/carplay.md), [Game Center](references/technologies/game-center.md), [Generative AI](references/technologies/generative-ai.md), [HealthKit](references/technologies/healthkit.md), [HomeKit](references/technologies/homekit.md), [iCloud](references/technologies/icloud.md), [ID Verifier](references/technologies/id-verifier.md), [iMessage apps and stickers](references/technologies/imessage-apps-and-stickers.md), [Live Photos](references/technologies/live-photos.md), [Mac Catalyst](references/technologies/mac-catalyst.md), [Machine learning](references/technologies/machine-learning.md), [Maps](references/technologies/maps.md), [NFC](references/technologies/nfc.md), [Photo editing](references/technologies/photo-editing.md), [ResearchKit](references/technologies/researchkit.md), [SharePlay](references/technologies/shareplay.md), [ShazamKit](references/technologies/shazamkit.md), [Sign in with Apple](references/technologies/sign-in-with-apple.md), [Siri](references/technologies/siri.md), [Tap to Pay on iPhone](references/technologies/tap-to-pay-on-iphone.md), [VoiceOver](references/technologies/voiceover.md), [Wallet](references/technologies/wallet.md)
