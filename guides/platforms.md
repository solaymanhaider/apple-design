# Platforms: what changes on each Apple platform

One section per platform, built from the "Designing for" pages and the Platform considerations sections across the HIG.
Use it in the platform adaptation pass of [workflow.md](workflow.md). Numbers are in points.

## Comparison at a glance

| | iOS | iPadOS | macOS | tvOS | visionOS | watchOS |
|---|---|---|---|---|---|---|
| Display | Medium, handheld | Large, held or on a stand, about 3 ft | Large, multiple displays, desk | Very large, 8 ft or more away | Infinite 3D canvas, about 2 m default | Small, wrist, about 1 ft |
| Primary input | Multi-Touch, virtual keyboard, voice | Touch, keyboard, trackpad, Apple Pencil, voice | Keyboard and pointer; trackpad gestures; touch on touch displays | Siri Remote, game controller, voice | Eyes plus indirect hand gestures; direct touch | Digital Crown, tap, swipe, drag, Action button, double tap |
| Session | Minutes, frequent switching | Minutes to hours, multiple apps | Minutes to hours of deep work, many apps | Hours, shared room, picture in picture | Varies, Shared Space or Full Space | Seconds, glanceable |
| Body text | 17 | 17 | 13 | 29 | 17 (bolder styles) | 16 |
| Control size (default / min) | 44 / 28 | 44 / 28 | 28 / 20 | 66 / 56 | 60 / 28 | 44 / 28 |
| Dynamic Type | Yes | Yes | No | Yes | Yes | Yes |
| Top-level navigation | Bottom tab bar | Top tab bar, convertible to sidebar | Sidebar in split view | Top tab bar (68 pt) | Vertical tab bar, leading side | Vertical tab view or list |
| Windows | One | Full screen or windowed, resizable, multiple | Multiple, main/key/inactive states, menu bar | One screen | Windows (glass) and volumes | One screen |
| Materials | Liquid Glass bars; ultraThin to thick | Same as iOS | Liquid Glass bars; vibrancy | Translucent tab bar | Fixed glass window background | Materials for hierarchy |
| Dark Mode | Yes | Yes | Yes | Yes | n/a (dark values) | Always dark |
| Haptics | Yes | Limited | Trackpad | No | No (uses sound) | Yes |
| System surfaces | Widgets, Live Activities, quick actions, Spotlight, Shortcuts, Controls, notifications | Same plus multitasking, drag and drop, menu bar | Menu bar, Dock menu, file management, full screen, panels | Top Shelf, TV app integration, SharePlay, TV provider accounts | Shared Space, SharePlay with spatial Personas, ornaments | Complications, notifications, Always On, watch faces, Smart Stack widgets |

## iOS ([reference](../references/getting-started/designing-for-ios.md))

Best practices from Apple
- Limit onscreen controls so people concentrate on primary content; make secondary actions discoverable with minimal interaction.
- Adapt to orientation, Dark Mode, and Dynamic Type.
- Design for how people hold the phone: controls in the middle and bottom are easier to reach; support swipe back and swipe actions in list rows.
- With permission, use platform data and capabilities (payments, biometrics, location) instead of asking people to type.

Structure and components
- Tab bar floats at the bottom on Liquid Glass; it can minimize on scroll with an accessory (like a mini player) and can include a search tab at the trailing end. Prefer 3 to 5 tabs; avoid the More tab.
- Toolbar at the top (navigation bar) with large title that collapses on scroll; only the most important items, the rest in a More menu; optional bottom toolbar with search when there is room.
- Split views only in regular width; popovers only in regular width (use sheets in compact width).
- Sheets: Cancel leading, Done trailing; medium and large detents with a grabber; swipe to dismiss.
- Action sheets for choices after an action; alerts for critical interruptions; menus in small, medium, or large layouts.
- Buttons can show an activity indicator for actions that take time.
- Status bar: obscure content beneath it; hide only temporarily for full-screen media.
- Home Screen quick actions, widgets (small, medium, large, extra large), Live Activities, Controls, App Shortcuts, Spotlight.

Inputs
- Standard gestures plus three-finger swipe (undo/redo), three-finger pinch (copy/paste), shake (undo).
- Virtual keyboards matched to the content type; Scribble and Apple Pencil on iPad.

## iPadOS ([reference](../references/getting-started/designing-for-ipados.md))

Best practices from Apple
- Use the large display to elevate content, minimizing modality and full-screen transitions; put controls where they are easy to reach but out of the way.
- Size and density follow viewing distance and input mode.
- Support Multi-Touch, keyboard and trackpad, and Apple Pencil, including combined interactions.
- Adapt to orientation, multitasking, Dark Mode, Dynamic Type, and running on macOS.

Structure and components
- Tab bar at the top, fixed or convertible to a sidebar (sidebarAdaptable); let people customize tabs when there are many sections; for a sidebar only, use NavigationSplitView.
- Toolbar can share the top row with the tab bar; customizable toolbars; the system adds the overflow menu when items do not fit.
- Windows: full screen or windowed; resizable with size and position remembered; window controls sit on the leading edge of the toolbar so leading toolbar buttons must move inward; pinch to open content in a new window.
- Two or three column split views; handle narrow, compact, and intermediate widths.
- Sheets use page or form presentation; popovers in regular width.
- Menu bar on iPad with the same menus and order as macOS; keyboard shortcuts follow macOS patterns; keyboard navigation in text, lists, and sidebars but not for buttons and switches.
- Pointer: system pointer effects, contiguous hit regions in bars, padding around interactive elements, hover to reveal minimized controls, multiple selection by dragging.
- Four-finger swipe switches apps; drag and drop between apps is expected.

## macOS ([reference](../references/getting-started/designing-for-macos.md))

Best practices from Apple
- Use large displays to show more content with fewer nested levels and less modality, at a comfortable density.
- Let people resize, hide, show, and move windows; support full-screen mode.
- Put every command in the menu bar; support keyboard shortcuts and keyboard-only work.
- Support high-precision input for pixel-perfect edits.
- Support trackpad and touch-display gestures with larger tap targets and controls that expand on touch, while keeping control size and density unchanged for keyboard and pointer.
- Allow personalization: customizable toolbars, window configurations, colors and fonts.

Window anatomy and states
- Frame (title bar, window controls, toolbar, rare bottom bar) plus body. Avoid critical content in a bottom bar or at the window bottom.
- States: main (frontmost, one per app), key (accepts input, one on screen), inactive. Use system appearances so the states read correctly; inactive windows lose vibrancy.
- Use the word "window" in user-facing text. Never build custom window frames or controls.

Menu bar (order is fixed)
App menu (About first, then Settings…, app items, Services, Hide, Hide Others, Show All, Quit), File (New, Open, Open Recent, Close, Save, Duplicate, Rename…, Move To…, Export As…, Revert To, Page Setup…, Print…), Edit (Undo, Redo, Cut, Copy, Paste, Paste and Match Style, Delete, Select All, Find, Spelling and Grammar, Substitutions, Transformations, Speech, Start Dictation, Emoji & Symbols), Format (Font, Text), View (Show/Hide Tab Bar, Show All Tabs, Show/Hide Toolbar, Customize Toolbar, Show/Hide Sidebar, Enter/Exit Full Screen), app-specific menus, Window (Minimize, Zoom, tab commands, Merge All Windows, Bring All to Front, open windows alphabetically), Help. Keep every item visible and disable rather than hide; one-word menu titles; standard shortcuts; show/hide items reflect the current state; provide View and Window menus even for minimal apps. Full tables are in [The menu bar](../references/components/menus-and-actions/the-menu-bar.md).

Components
- Toolbar in the window frame, items without bezels, titles inline with controls; every toolbar item also in the menu bar; customizable.
- Sidebar in small, medium, or large size (user setting), collapses when the window shrinks, two levels of hierarchy max, icons follow the accent color.
- Split views with 1 pt dividers, min and max pane sizes, multiple ways to reveal hidden panes.
- Buttons: push buttons (ellipsis when they open another window), square (gradient) buttons for table add and remove, help buttons (one per window, in the view not the frame), image buttons with about 10 px padding.
- Tables: sortable column headings, resizable columns, alternating row colors, outline views for hierarchy.
- Sheets dim the parent window; people can still use other windows. Panels for repeated input (find and replace, inspectors, Colors, Fonts). Popovers can detach into panels.
- Alerts: caution symbol only when extra attention is needed.
- Dock menu with high-value items that are also available elsewhere.
- Typography: 13 pt body, dynamic font variants for controls, no Dynamic Type.
- Color: the person's accent color overrides yours unless the system setting is multicolor; fixed-color sidebar icons are the exception.
- Touch displays: tap targets enlarge, not controls; essential hidden controls also in a context menu; reveal hidden controls on tap of their location; keep selection when revealing.

## tvOS ([reference](../references/getting-started/designing-for-tvos.md))

Best practices from Apple
- Fluid, familiar Siri Remote gestures.
- Embrace the focus system: focused items highlight and expand; people always know where they are.
- Edge-to-edge artwork, subtle fluid animation, engaging audio, legible from across the room.
- Multiuser: easy infrequent sign-in, shared sign-in, automatic profile switching.

Specifics
- Safe area 60 pt top and bottom, 80 pt sides; padding for focus growth; grid widths published for 2 to 9 columns with 40 pt horizontal and 100 pt minimum vertical spacing.
- Tab bar at the top, 68 pt tall, 46 pt from the top edge, translucent with only the selected tab opaque; scrolls off screen on single-view tabs, pinned when a tab contains a split view; live-viewing apps order tabs Live, Cloud DVR, Other.
- Body 29 pt, minimum 23 pt; text styles from Title 1 (76 pt) to Caption 2 (23 pt), all Medium weight.
- Controls 66 pt default, 56 pt minimum. Focus shown by scale and motion, never only color.
- Split view one third / two thirds or half and half with a single title above.
- Layered app icon (2 to 5 layers, 800x480 px) with parallax and a safe zone; layered images in Top Shelf.
- Live-viewing apps autoplay after a few seconds; integrate with the TV app; Top Shelf features new and personalized content, no ads or prices.
- Search with on-screen suggestions because typing is slow.

## visionOS ([reference](../references/getting-started/designing-for-visionos.md))

Best practices from Apple
- Embrace space, Spatial Audio, immersion, passthrough, and eye and hand input.
- Choose the minimum level of immersion each key moment needs: window, mixed, progressive, or full.
- Use windows for contained UI-centric experiences; volumes for bounded 3D content; immersive spaces for meaningful moments.
- Prioritize comfort: content within the field of view and relative to the head position, no jarring motion, indirect gestures with hands resting, direct gestures only within reach and briefly, no required movement.
- Support SharePlay with spatial Personas.

Specifics
- Default window 1280x720 pt about 2 m away with a fixed glass background; set min and max sizes; shape suits content; minimize 3D depth inside windows.
- Vertical tab bar on the leading side that expands on gaze; symbol plus short label per tab; a sidebar inside a tab for deep hierarchies.
- Toolbar along the bottom edge in front of the window; symbol or text per item, label revealed on gaze; no vertical toolbars; no pull-down menus in toolbars; keep windows wider than the toolbar.
- Ornaments for frequently needed window controls; supplemental content goes in an adjacent window or split view, not an ornament.
- Buttons: circle for icon-only, capsule or rounded rectangle for text; sizes mini 28, small 32, regular 44, large 52, extra large 64; centers at least 60 pt apart; thin material background on glass windows, glass when floating; white fill with black content is reserved for the toggled state; standard controls play sound (no haptics).
- Sheets centered in the field of view, not from the bottom; alerts and menus near the content they affect; prefer the subtle breakthrough effect for menus.
- Text: 17 pt body with bolder weights, Extra Large Title 1 and 2, prefer 2D text, bold when floating without background, billboard toward the viewer.
- Color sparingly on glass, in bold text and large areas; system colors use the dark values.
- Eyes: rounded interactive shapes, a containing shape for multi-element components, enough space around targets, no repeating patterns across the view, standard hover effects (custom ones only for special moments).
- Gestures: indirect tap, pinch and hold, drag; direct touch, touch and hold, double touch, swipe, two-hand zoom and rotate; custom gestures only in a Full Space with permission, no specific-hand or body-position requirements, keep hands free for system overlays, avoid the hand-roll motion.
- Spatial layout: center important content, depth for hierarchy not text, fixed scale for real objects, dynamic scale for legibility, few windows, Digital Crown recenters.
- Immersion rules in [foundations.md](foundations.md) under Immersive experiences.

## watchOS ([reference](../references/getting-started/designing-for-watchos.md))

Best practices from Apple
- Quick, glanceable, single-screen interactions with one or two gestures.
- Shallow hierarchy; Digital Crown for vertical navigation and switching screens.
- Proactively personalize with on-device data for what matters now or soon.
- Complications on the watch face with deep links; notifications with actions; background color and materials for meaning and hierarchy.
- The app must work on its own, complementing complications and notifications.

Specifics
- Body 16 pt (SF Compact), minimum 12 pt; text styles from Large Title 36 pt down to Footnote 2 at 12 pt for 40 to 42 mm; sizes per case size in the Typography reference; 140 percent text enlargement target.
- Controls 44 pt default, 28 pt minimum; full-width capsule buttons for primary actions; at most three glyph buttons or two text buttons per row; same height for stacked buttons.
- Toolbar buttons in the top corners or a scrolling toolbar button revealed at the top of the content; Liquid Glass applied automatically.
- Vertical tab views with page controls beside the Digital Crown; split views show list or detail full screen; detail pages in a vertical tab view.
- Sheets are full-screen semitransparent overlays for custom modal tasks only; alerts and action sheets (max four buttons including Cancel) for choices.
- No indeterminate progress indicators; show determinate progress or a status message.
- Double tap performs the view's primary action (not in scrolling or list views); Action button starts an essential action.
- Always On: keep showing useful state when the wrist drops; Smart Stack widgets, complications across all families, shareable watch faces.
- App icon circular, 1088 px canvas, no black background.

## iPhone Duo ([reference](../references/getting-started/designing-for-iphone-duo.md))

- Two displays (outer and inner), many poses, and Split View multitasking: build to resize with size classes, layout margins, and safe areas; no fixed widths.
- Keep functionality and state identical across displays; the inner display may show one more level of hierarchy (Mail: list and message side by side).
- Toolbars, tab bars, and navigation controls move to the side (vertical) on the outer display and in landscape on the inner display; follow the standard vertical order (Back or Close at the top, then prominent actions like Done, then the remaining groups); prioritize items for overflow; group with the system's grouping APIs; use the system overflow menu; keep controls near the content they affect; account for asymmetry.
- Reserved regions: outer camera (always, expands for Live Activities), inner camera (only when active), folding region (when partially open). Prefer containers that adapt automatically; even column counts in grids; small adjustments on fold, not rearrangement.
- Arrangement views (split or overlay) for two-view layouts; keep navigation containers outside them.
- Games: playable in every pose; fill the screen; prefer changing aspect ratio over letterboxing; decorate any padding.

## Games on Apple platforms ([reference](../references/getting-started/designing-for-games.md))

- Playable right after install (initial download 30 minutes or less, more in the background); great defaults; teach through play; defer permission and other requests.
- Text always legible at each platform's minimum size; buttons at least the platform minimum (44 pt on iOS); resolution-independent assets; safe areas and device features respected; menus adapt to aspect ratios; design for full screen.
- Support each platform's default interaction and physical controllers with alternatives; touch controls that embrace the touchscreen.
- Perceivability, personalization (type size, control mapping, motion intensity, sound balance), self-representation, no stereotypes.
- Game Center, GameSave for cross-device progress, Core Haptics, and other Apple technologies for unique mechanics.
