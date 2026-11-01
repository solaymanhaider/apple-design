# Applying Apple's guidelines to web apps

Apple's Human Interface Guidelines are written for Apple platforms, not the web. This guide is a **translation**: it
keeps Apple's rules, numbers, and component behaviors and maps them onto HTML, CSS, and ARIA so a web app feels like
an Apple-designed product. Everything here that is not a direct HIG rule is marked as a translation decision.

## Principles that carry over unchanged

- Content first, controls recede; branding defers to content; no logo wallpaper.
- Order by importance in reading order; group with space; progressive disclosure.
- Use the platform's conventions. On the web that means native elements and expected keyboard behavior, the same way Apple asks for system components.
- One accent color used sparingly for the primary action and selection; semantic colors for everything else; nothing conveyed by color alone.
- Minimum contrast 4.5:1 (3:1 for 18 px or bold), target 7:1 for custom pairs; light and dark appearances both required; respect the system appearance, no in-app theme switch.
- Hit targets 44x44 CSS px on touch; 28x28 px minimum for pointer-only desktop controls; about 12 px padding between bezeled controls, 24 px between bezel-less ones.
- Text scales with the person's settings; never below 11 px (mobile) or 10 px (desktop); 17 px body on mobile, 13 px body for dense desktop tools, or 16 to 17 px for reading-oriented desktop pages (translation decision: Apple's 13 pt macOS body assumes a 2x display at desk distance; for browser pages aim at 15 to 17 px unless building a dense tool).
- Motion is purposeful, brief, cancelable, and disabled under `prefers-reduced-motion`.
- Modals only with a clear benefit, one at a time, always dismissible, confirmation before data loss.
- Copy: verbs on buttons, title case for buttons and menu items, sentence case for body, clear error text next to the field, no "Click here".

## Responsive structure mapped from size classes

Apple decides layout by size class, not device. Do the same with container or viewport queries. A single breakpoint set that mirrors compact and regular width:

| Width | Treat as | Navigation | Presentation |
|---|---|---|---|
| Under about 700 px | Compact (iPhone) | Bottom tab bar (3 to 5 items, labels, filled symbols when selected), top bar with large title that collapses on scroll, Back as a chevron | Sheets slide up from the bottom, full-height or half-height; no popovers; action sheets for choices after an action |
| About 700 to 1000 px | Regular (iPad) | Tab bar at the top or a collapsible sidebar; toolbar shares the top row | Centered sheets (form sheet), popovers anchored to controls |
| Over about 1000 px | Regular, desktop (Mac) | Sidebar with two levels max in a resizable split view; toolbar with at most three groups; command menu bar equivalent (a "..." or app menu) if the app is document-centric | Dialogs centered; popovers; panels for inspectors |

Translation decision: the breakpoint values are approximations of where Apple devices change size class; tune them to your content. The behaviors in each column are HIG rules.

Functionality must not change with width; only how much is visible at once. Switch a tab bar into a sidebar when width grows (Layout, Tab bars).

## CSS tokens

A starting stylesheet that encodes Apple's published values. Colors are Apple's system color values converted to hex (design reference only; Apple may change them).

```css
:root {
  color-scheme: light dark;

  /* Type: the system font stack renders SF on Apple devices. */
  --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-serif: "New York", ui-serif, Georgia, serif;
  --font-mono: "SF Mono", ui-monospace, Menlo, Consolas, monospace;

  /* iOS text styles at the default (Large) size: size / line-height / weight. */
  --text-large-title: 600 34px/41px var(--font-sans);
  --text-title1:      400 28px/34px var(--font-sans);
  --text-title2:      400 22px/28px var(--font-sans);
  --text-title3:      400 20px/25px var(--font-sans);
  --text-headline:    600 17px/22px var(--font-sans);
  --text-body:        400 17px/22px var(--font-sans);
  --text-callout:     400 16px/21px var(--font-sans);
  --text-subhead:     400 15px/20px var(--font-sans);
  --text-footnote:    400 13px/18px var(--font-sans);
  --text-caption1:    400 12px/16px var(--font-sans);
  --text-caption2:    400 11px/13px var(--font-sans);

  /* Sizing from the HIG. */
  --hit-target: 44px;        /* 60px for gaze-driven UI, 28px desktop minimum */
  --control-gap-bezel: 12px;
  --control-gap-plain: 24px;
  --gutter-compact: 16px;    /* convention, not HIG */
  --gutter-regular: 20px;    /* convention, not HIG */

  /* System colors, light. */
  --red: #FF383C; --orange: #FF8D28; --yellow: #FFCC00; --green: #34C759; --mint: #00C8B3;
  --teal: #00C3D0; --cyan: #00C0E8; --blue: #0088FF; --indigo: #6155F5; --purple: #CB30E0;
  --pink: #FF2D55; --brown: #AC7F5E;
  --gray: #8E8E93; --gray2: #AEAEB2; --gray3: #C7C7CC; --gray4: #D1D1D6; --gray5: #E5E5EA; --gray6: #F2F2F7;

  /* Semantic roles (translation of iOS dynamic colors). */
  --accent: var(--blue);
  --label: rgba(0,0,0,1);
  --label-secondary: rgba(60,60,67,0.6);
  --label-tertiary: rgba(60,60,67,0.3);
  --label-quaternary: rgba(60,60,67,0.18);
  --placeholder: rgba(60,60,67,0.3);
  --separator: rgba(60,60,67,0.29);
  --separator-opaque: #C6C6C8;
  --link: var(--blue);
  --bg: #FFFFFF;                 /* system background, primary */
  --bg-secondary: #F2F2F7;
  --bg-tertiary: #FFFFFF;
  --bg-grouped: #F2F2F7;         /* grouped background, primary */
  --bg-grouped-secondary: #FFFFFF;
  --bg-grouped-tertiary: #F2F2F7;
}

@media (prefers-color-scheme: dark) {
  :root {
    --red: #FF4245; --orange: #FF9230; --yellow: #FFD600; --green: #30D158; --mint: #00DAC3;
    --teal: #00D2E0; --cyan: #3CD3FE; --blue: #0091FF; --indigo: #6D7CFF; --purple: #DB34F2;
    --pink: #FF375F; --brown: #B78A66;
    --gray: #8E8E93; --gray2: #636366; --gray3: #48484A; --gray4: #3A3A3C; --gray5: #2C2C2E; --gray6: #1C1C1E;
    --label: rgba(255,255,255,1);
    --label-secondary: rgba(235,235,245,0.6);
    --label-tertiary: rgba(235,235,245,0.3);
    --label-quaternary: rgba(235,235,245,0.16);
    --placeholder: rgba(235,235,245,0.3);
    --separator: rgba(84,84,88,0.6);
    --separator-opaque: #38383A;
    --bg: #000000; --bg-secondary: #1C1C1E; --bg-tertiary: #2C2C2E;
    --bg-grouped: #000000; --bg-grouped-secondary: #1C1C1E; --bg-grouped-tertiary: #2C2C2E;
  }
}

@media (prefers-contrast: more) {
  :root {
    --red: #E9152D; --orange: #C55300; --yellow: #A16A00; --green: #008932; --mint: #008575;
    --teal: #008198; --cyan: #007EAE; --blue: #1E6EF4; --indigo: #564ADE; --purple: #B02FC2;
    --pink: #E7124D; --brown: #956D51;
  }
}
@media (prefers-contrast: more) and (prefers-color-scheme: dark) {
  :root {
    --red: #FF6165; --orange: #FFA056; --yellow: #FEDF43; --green: #4AD968; --mint: #54DFCB;
    --teal: #3BDDEC; --cyan: #6DD9FF; --blue: #5CB8FF; --indigo: #A7AAFF; --purple: #EA8DFF;
    --pink: #FF8AC4; --brown: #DBA679;
  }
}

html { font: var(--text-body); color: var(--label); background: var(--bg); -webkit-font-smoothing: antialiased; }
body { margin: 0; }
```

Notes
- The twelve system colors and six grays, in light, dark, and increased-contrast variants, are Apple's published values. The label, separator, and background values are a translation of the iOS dynamic colors (Apple publishes their roles, not their numbers, in the HIG) and match the commonly observed system values; treat them as a reasonable default.
- Use `rem` units if you want text to follow browser zoom and the OS text size; the pixel values above are the Large (default) Dynamic Type sizes, which map to 1 rem = 17 px on mobile. Test layouts at 200 percent text size (Apple's target) and let rows grow and columns collapse rather than truncating.

## Materials on the web

Apple's rule: Liquid Glass belongs to the floating controls layer (bars, sidebars, popovers, alerts), never to content. Translation:

```css
.bar {
  position: sticky; top: 0;
  background: color-mix(in srgb, var(--bg) 70%, transparent);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 0.5px solid var(--separator);
}
.bar--over-media {                     /* clear variant: only over photos or video */
  background: rgba(0,0,0,0.35);        /* Apple's 35% dimming layer for bright media */
  color: #fff;
}
@media (prefers-reduced-transparency: reduce) {
  .bar { background: var(--bg); backdrop-filter: none; -webkit-backdrop-filter: none; }
}
```

- Let content scroll beneath bars (no opaque bar fills); add a soft "scroll edge" fade instead of a solid background.
- Content-layer grouping uses plain semantic backgrounds (grouped background colors), not blur.
- Keep the bar's text and symbols monochrome; tint only the single primary action's background.

## Component mapping

Each row keeps Apple's behavior rules; the element and ARIA columns are the translation.

| Apple component | HTML / ARIA | Behavior to preserve |
|---|---|---|
| Tab bar | `<nav aria-label="Primary">` with `<a aria-current="page">` items; fixed bottom on compact, top or sidebar on regular | Navigation only, never actions; always visible except under a modal; 3 to 5 items; single-word labels; symbol plus label; badges for critical info only |
| Sidebar | `<nav>` inside a resizable `<aside>`; disclosure groups with `<details>` or `aria-expanded` | Two levels max; collapsible; selection persistently highlighted; icons in the accent color |
| Toolbar / navigation bar | `<header role="toolbar">`; Back as a chevron link; title `<h1>` | At most three groups; one prominent primary action on the trailing side; overflow into a "More" menu; title under 15 characters, never the app name |
| Split view | CSS grid with a draggable 1 px divider (`role="separator" aria-orientation="vertical"`) | Persist selection in each pane; collapse to a stack in compact width |
| List / table | `<ul>` or `<table>` with `<th scope="col">` | Text in rows; sortable and resizable columns on desktop; alternating row colors for wide tables; detail disclosure (info button) only for more info, not navigation |
| Collection | CSS grid of cards | Visual items, consistent sizes, easy selection |
| Button | `<button>`; `.prominent` for the accent-filled primary | 44 px target; visible pressed state; one or two prominent buttons per view; verbs, title case; style not size shows preference |
| Pop-up button | `<select>` or a listbox menu button | Flat list of mutually exclusive options; shows the current value; useful default |
| Pull-down button | `<button aria-haspopup="menu">` plus `role="menu"` | Commands related to the label; not a dumping ground; succinct menu title only if it adds meaning |
| Menu / context menu | `role="menu"`, `role="menuitem"`, separators, submenus one level deep | Important items first; groups by separators; icons all or none per group; disabled items stay visible; ellipsis when more input follows; context menu items also available elsewhere |
| Segmented control | `role="radiogroup"` of `role="radio"` buttons, or `role="tablist"` when switching views | 2 to 5 segments, consistent content type, equal widths where possible |
| Toggle | `<button role="switch" aria-checked>` or `<input type="checkbox" switch>` | Two opposing states with an obvious difference; switch style only in list rows, checkbox elsewhere |
| Slider | `<input type="range">` | Continuous values, familiar direction, optional paired text field and stepper; never for volume on Apple platforms |
| Stepper | Two buttons plus a read-only value or paired text field | For small increments; obvious target value |
| Text field | `<label>` + `<input>` with `placeholder` as hint, `autocomplete`, correct `type` and `inputmode` | Short text; hint shows format; secure fields for secrets, never prepopulated; inline error beside the field |
| Text view | `<textarea>` or contenteditable | Long or formatted text; legible; selectable |
| Search field | `<input type="search">` inside `<form role="search">` | Placeholder states scope; results as you type; suggestions and recents; scope bar (tabs or chips) and tokens to filter; one search location |
| Alert | `<dialog role="alertdialog">` | Critical and actionable only; title says what and why; two buttons, default trailing, Cancel leading; destructive styling; no "OK" unless informational; never on page load |
| Action sheet | `<dialog>` anchored to the bottom on compact widths | Choices after an intentional action; destructive first; Cancel last; no scrolling |
| Sheet | `<dialog>` as bottom sheet (compact) or centered form (regular) | One at a time; Cancel leading, Done trailing; Done always paired with Cancel or Back; swipe or Esc to dismiss; confirm before losing changes |
| Popover | Popover API or `role="dialog"` anchored to its trigger | Regular width only; small focused content; auto-closes on outside click and saves work; never for warnings; one at a time |
| Progress indicator | `<progress>` with a value whenever possible; indeterminate only when unavoidable | Keep moving; switch to determinate when you can; label what is happening |
| Activity indicator in a button | Button shows a spinner and a status label, stays disabled | For actions that do not complete instantly |
| Badge | Small red pill with white text | Critical new information only |
| Notification / Live Activity | Web push with concise text; toast for in-app status | Timely, high value, never promotional, never an error message, never "open the app to..." |

## Keyboard and pointer

- Full keyboard operability: Tab order follows reading order, visible focus ring (Apple's keyboard focus indicator is the accent color), Esc cancels dialogs and popovers, Enter activates the default button, Space toggles.
- Standard shortcuts people know from Apple platforms: Command-F find, Command-Z and Shift-Command-Z undo and redo, Command-S save, Command-N new, Command-Comma settings, Command-Question mark help, Command-Period cancel. Use `metaKey` on Apple devices and `ctrlKey` elsewhere; never repurpose the system's own shortcuts.
- Hover states on pointer devices only (`@media (hover: hover)`); enlarge hit areas rather than controls on touch.
- Support swipe back and swipe actions in list rows on touch where it fits; never make a gesture the only way.

## Accessibility checklist for web

1. Landmarks and headings follow the information hierarchy; one `<h1>` per view that matches the toolbar title.
2. Every image and icon has alt text or `aria-hidden="true"` when decorative; icon-only buttons have `aria-label`.
3. Color contrast 4.5:1 minimum; test light, dark, and `prefers-contrast: more`.
4. Text scales to 200 percent without clipping; rows grow, columns stack.
5. `prefers-reduced-motion` removes nonessential animation; `prefers-reduced-transparency` removes blur.
6. All functionality works with keyboard alone and with a screen reader; dialogs trap and restore focus; live regions announce status.
7. No time-limited UI without a way to extend; no autoplaying media without controls; a way to disable flashing content.
8. Right-to-left support with logical properties (`margin-inline-start`, `inset-inline`) and mirrored directional icons.

## What does not translate

- Liquid Glass lensing and refraction, system-managed hover effects, haptics, Dynamic Island, widgets, complications, App Shortcuts, and Spotlight have no web equivalent; use the closest honest substitute (push notifications, home screen web app icons) and do not fake system UI.
- Do not imitate Apple system UI chrome pixel for pixel or use Apple trademarks, SF Symbols in logos, or Apple hardware imagery (SF Symbols are licensed for use on Apple platforms; on the web use an icon set with similar weights and the same metaphors).
- A web app rendered inside a native app should follow the Web views component rules: support back and forward, never use a web view to build a browser, and make the content feel native.
