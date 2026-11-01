# Design tokens and specifications

Every number on this page comes from Apple's Human Interface Guidelines. The source page is named for each table
so you can verify it. Values are in points (pt) unless stated. Apple warns that documented color values are for
design reference only and may change between OS releases: in native apps use the semantic API, never a hard-coded value.
Where this page adds a convention that Apple does not state, it is marked **Convention (not HIG)**.

## 1. Sizing and spacing

### Control sizes (source: [Accessibility](../references/foundations/accessibility.md))

| Platform | Default control size | Minimum control size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Buttons specifically: a hit region of at least 44x44 pt, and 60x60 pt in visionOS ([Buttons](../references/components/menus-and-actions/buttons.md)).

### Spacing between controls (source: Accessibility)

- About 12 pt of padding around elements that have a bezel.
- About 24 pt of padding around the visible edges of elements without a bezel.
- visionOS: place buttons so their centers are at least 60 pt apart; if buttons are 60 pt or larger, add 4 pt of padding around them so hover effects do not overlap ([Buttons](../references/components/menus-and-actions/buttons.md), [Layout](../references/foundations/layout.md)).
- macOS image buttons: about 10 px of padding between the image edge and the button edge.
- watchOS: no more than three glyph buttons, or two text buttons, side by side in a row ([Layout](../references/foundations/layout.md)).

### Safe areas and margins

- Always lay out inside the system safe area and layout guides (hardware features, status bar, toolbars, tab bars, Dynamic Island). Apple does not publish fixed margin numbers for iOS, iPadOS, or macOS; use the system layout margins and readable-content guide ([Layout](../references/foundations/layout.md)).
- tvOS: inset primary content 60 pt from top and bottom and 80 pt from the sides.
- macOS: avoid controls or critical information at the bottom of a window; avoid content behind the camera housing.
- visionOS: default window size 1280x720 pt, placed about 2 m from the wearer ([Windows](../references/components/presentation/windows.md)); keep reading content at least 1 m away ([Eyes](../references/inputs/eyes.md)).
- **Convention (not HIG):** when a web or cross-platform layout needs a fixed margin, 16 pt side gutters on compact widths and 20 pt on regular widths match what the system layout margins typically resolve to. Verify against the real platform before shipping.

### tvOS grid layouts (source: [Layout](../references/foundations/layout.md))

| Columns | Unfocused content width | Horizontal spacing | Minimum vertical spacing |
|---|---|---|---|
| Two | 860 pt | 40 pt | 100 pt |
| Three | 560 pt | 40 pt | 100 pt |
| Four | 410 pt | 40 pt | 100 pt |
| Five | 320 pt | 40 pt | 100 pt |
| Six | 260 pt | 40 pt | 100 pt |
| Seven | 217 pt | 40 pt | 100 pt |
| Eight | 184 pt | 40 pt | 100 pt |
| Nine | 160 pt | 40 pt | 100 pt |

tvOS tab bar: height 68 pt, top edge 46 pt from the top of the screen, not changeable ([Tab bars](../references/components/navigation-and-search/tab-bars.md)).

### visionOS button sizes (source: [Buttons](../references/components/menus-and-actions/buttons.md))

Mini 28 pt, Small 32 pt, Regular 44 pt, Large 52 pt, Extra large 64 pt. Circular buttons exist at every size; capsule (text only) and rounded rectangle at Small, Regular, Large; capsule (text and icon) at Regular and Large.

### Split view dividers

macOS thin divider is 1 pt wide; prefer it ([Split views](../references/components/layout-and-organization/split-views.md)). tvOS default split is one third primary, two thirds secondary.

### Toolbar titles

Keep a window or view title under 15 characters. Never title a window with the app name ([Toolbars](../references/components/menus-and-actions/toolbars.md)). App menu short name: 16 characters or fewer ([The menu bar](../references/components/menus-and-actions/the-menu-bar.md)).

## 2. Typography

### Fonts

- System fonts: **SF Pro** (iOS, iPadOS, macOS, tvOS, visionOS), **SF Compact** (watchOS; SF Compact Rounded in complications), **New York** (serif, available on all platforms; needs explicit styles on visionOS), plus SF Mono and rounded variants. Download from https://developer.apple.com/fonts/ for mockups; in code use the system font APIs, never embed the system fonts.
- Prefer Regular, Medium, Semibold, Bold. Avoid Ultralight, Thin, Light, especially at small sizes.
- Minimize the number of typefaces. Use the built-in text styles so Dynamic Type works. macOS does not support Dynamic Type.
- Support text enlargement of at least 200 percent (140 percent in watchOS).

### Default and minimum sizes (source: [Typography](../references/foundations/typography.md))

| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

### iOS and iPadOS text styles at the default (Large) Dynamic Type size

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

Dynamic Type sizes run xSmall, Small, Medium, Large (default), xLarge, xxLarge, xxxLarge, then accessibility sizes AX1 to AX5. At AX5, Body is 53 pt and Large Title is 60 pt. The full tables for every size are in the Typography reference. visionOS uses bolder body and title styles and adds Extra Large Title 1 and 2.

### macOS text styles

| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

macOS dynamic font variants for matching standard controls (NSFont):

| Dynamic font variant | API |
|---|---|
| Control content | controlContentFont(ofSize:)) |
| Label | labelFont(ofSize:)) |
| Menu | menuFont(ofSize:)) |
| Menu bar | menuBarFont(ofSize:)) |
| Message | messageFont(ofSize:)) |
| Palette | paletteFont(ofSize:)) |
| Title | titleBarFont(ofSize:)) |
| Tool tips | toolTipsFont(ofSize:)) |
| Document text (user) | userFont(ofSize:)) |
| Monospaced document text (user fixed pitch) | userFixedPitchFont(ofSize:)) |
| Bold system font | boldSystemFont(ofSize:)) |
| System font | systemFont(ofSize:)) |

### tvOS text styles

| Text style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Title 1 | Medium | 76 | 96 | Bold |
| Title 2 | Medium | 57 | 66 | Bold |
| Title 3 | Medium | 48 | 56 | Bold |
| Headline | Medium | 38 | 46 | Bold |
| Subtitle 1 | Regular | 38 | 46 | Medium |
| Callout | Medium | 31 | 38 | Bold |
| Body | Medium | 29 | 36 | Bold |
| Caption 1 | Medium | 25 | 32 | Bold |
| Caption 2 | Medium | 23 | 30 | Bold |

### watchOS text styles at the default size for 40mm/41mm/42mm

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 36 | 38.5 | Bold |
| Title 1 | Regular | 34 | 36.5 | Semibold |
| Title 2 | Regular | 28 | 30.5 | Semibold |
| Title 3 | Regular | 19 | 21.5 | Semibold |
| Headline | Semibold | 16 | 18.5 | Semibold |
| Body | Regular | 16 | 18.5 | Semibold |
| Caption 1 | Regular | 15 | 17.5 | Semibold |
| Caption 2 | Regular | 14 | 16.5 | Semibold |
| Footnote 1 | Regular | 13 | 15.5 | Semibold |
| Footnote 2 | Regular | 12 | 14.5 | Semibold |

### Tracking

The system adjusts SF tracking automatically at every point size. For static mockups use the tracking table in the Typography reference (for example SF Pro: 12 pt = 0, 17 pt = -0.43 pt, 34 pt = +0.40 pt).

### Capitalization

- Title-style capitalization: button labels, menu items, menu titles, column headings, tab labels, alert button titles.
- Sentence-style capitalization: alert messages, body copy, descriptions, hints.
- Remove articles (a, an, the) from menu item labels. Append an ellipsis (…) when an item needs more input before it completes. ([Menus](../references/components/menus-and-actions/menus.md), [Writing](../references/foundations/writing.md))

## 3. Color

### Contrast minimums (source: [Accessibility](../references/foundations/accessibility.md), [Dark Mode](../references/foundations/dark-mode.md))

| Text size | Text weight | Minimum contrast ratio |
|---|---|---|
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |

Minimum contrast ratio in every appearance is 4.5:1. For custom foreground and background colors strive for 7:1, especially for small text. Never convey information with color alone.

### System colors (source: [Color](../references/foundations/color.md))

Hex values are converted from Apple's published RGB values. visionOS uses the default dark values.

| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Red | red | #FF383C (255, 56, 60) | #FF4245 (255, 66, 69) | #E9152D (233, 21, 45) | #FF6165 (255, 97, 101) |
| Orange | orange | #FF8D28 (255, 141, 40) | #FF9230 (255, 146, 48) | #C55300 (197, 83, 0) | #FFA056 (255, 160, 86) |
| Yellow | yellow | #FFCC00 (255, 204, 0) | #FFD600 (255, 214, 0) | #A16A00 (161, 106, 0) | #FEDF43 (254, 223, 67) |
| Green | green | #34C759 (52, 199, 89) | #30D158 (48, 209, 88) | #008932 (0, 137, 50) | #4AD968 (74, 217, 104) |
| Mint | mint | #00C8B3 (0, 200, 179) | #00DAC3 (0, 218, 195) | #008575 (0, 133, 117) | #54DFCB (84, 223, 203) |
| Teal | teal | #00C3D0 (0, 195, 208) | #00D2E0 (0, 210, 224) | #008198 (0, 129, 152) | #3BDDEC (59, 221, 236) |
| Cyan | cyan | #00C0E8 (0, 192, 232) | #3CD3FE (60, 211, 254) | #007EAE (0, 126, 174) | #6DD9FF (109, 217, 255) |
| Blue | blue | #0088FF (0, 136, 255) | #0091FF (0, 145, 255) | #1E6EF4 (30, 110, 244) | #5CB8FF (92, 184, 255) |
| Indigo | indigo | #6155F5 (97, 85, 245) | #6D7CFF (109, 124, 255) | #564ADE (86, 74, 222) | #A7AAFF (167, 170, 255) |
| Purple | purple | #CB30E0 (203, 48, 224) | #DB34F2 (219, 52, 242) | #B02FC2 (176, 47, 194) | #EA8DFF (234, 141, 255) |
| Pink | pink | #FF2D55 (255, 45, 85) | #FF375F (255, 55, 95) | #E7124D (231, 18, 77) | #FF8AC4 (255, 138, 196) |
| Brown | brown | #AC7F5E (172, 127, 94) | #B78A66 (183, 138, 102) | #956D51 (149, 109, 81) | #DBA679 (219, 166, 121) |

### iOS and iPadOS system grays

| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Gray | systemGray | #8E8E93 (142, 142, 147) | #8E8E93 (142, 142, 147) | #6C6C70 (108, 108, 112) | #AEAEB2 (174, 174, 178) |
| Gray (2) | systemGray2 | #AEAEB2 (174, 174, 178) | #636366 (99, 99, 102) | #8E8E93 (142, 142, 147) | #7C7C80 (124, 124, 128) |
| Gray (3) | systemGray3 | #C7C7CC (199, 199, 204) | #48484A (72, 72, 74) | #AEAEB2 (174, 174, 178) | #545456 (84, 84, 86) |
| Gray (4) | systemGray4 | #D1D1D6 (209, 209, 214) | #3A3A3C (58, 58, 60) | #BCBCC0 (188, 188, 192) | #444446 (68, 68, 70) |
| Gray (5) | systemGray5 | #E5E5EA (229, 229, 234) | #2C2C2E (44, 44, 46) | #D8D8DC (216, 216, 220) | #363638 (54, 54, 56) |
| Gray (6) | systemGray6 | #F2F2F7 (242, 242, 247) | #1C1C1E (28, 28, 30) | #EBEBF0 (235, 235, 240) | #242426 (36, 36, 38) |

### iOS and iPadOS semantic colors

Backgrounds come in two sets, system and grouped, each with primary, secondary, and tertiary levels. Use grouped backgrounds for grouped table views; use primary for the overall view, secondary for grouping within it, tertiary for grouping within secondary elements. Foreground colors:

| Color | Use for… | UIKit API |
|---|---|---|
| Label | A text label that contains primary content. | label |
| Secondary label | A text label that contains secondary content. | secondaryLabel |
| Tertiary label | A text label that contains tertiary content. | tertiaryLabel |
| Quaternary label | A text label that contains quaternary content. | quaternaryLabel |
| Placeholder text | Placeholder text in controls or text views. | placeholderText |
| Separator | A separator that allows some underlying content to be visible. | separator |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | opaqueSeparator |
| Link | Text that functions as a link. | link |

Never reassign a semantic color's meaning (no separator color as text, no secondary label as a background).

### macOS semantic colors (AppKit)

| Color | Use for… | AppKit API |
|---|---|---|
| Alternate selected control text color | The text on a selected surface in a list or table. | alternateSelectedControlTextColor |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | alternatingContentBackgroundColors |
| Control accent | The accent color people select in System Settings. | controlAccentColor |
| Control background color | The background of a large interface element, such as a browser or table. | controlBackgroundColor |
| Control color | The surface of a control. | controlColor |
| Control text color | The text of a control that is available. | controlTextColor |
| Current control tint | The system-defined control tint. | currentControlTint |
| Unavailable control text color | The text of a control that’s unavailable. | disabledControlTextColor |
| Find highlight color | The color of a find indicator. | findHighlightColor |
| Grid color | The gridlines of an interface element, such as a table. | gridColor |
| Header text color | The text of a header cell in a table. | headerTextColor |
| Highlight color | The virtual light source onscreen. | highlightColor |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | keyboardFocusIndicatorColor |
| Label color | The text of a label containing primary content. | labelColor |
| Link color | A link to other content. | linkColor |
| Placeholder text color | A placeholder string in a control or text view. | placeholderTextColor |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | quaternaryLabelColor |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | secondaryLabelColor |
| Selected content background color | The background for selected content in a key window or view. | selectedContentBackgroundColor |
| Selected control color | The surface of a selected control. | selectedControlColor |
| Selected control text color | The text of a selected control. | selectedControlTextColor |
| Selected menu item text color | The text of a selected menu. | selectedMenuItemTextColor |
| Selected text background color | The background of selected text. | selectedTextBackgroundColor |
| Selected text color | The color for selected text. | selectedTextColor |
| Separator color | A separator between different sections of content. | separatorColor |
| Shadow color | The virtual shadow cast by a raised object onscreen. | shadowColor |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | tertiaryLabelColor |
| Text background color | The background color behind text. | textBackgroundColor |
| Text color | The text in a document. | textColor |
| Under page background color | The background behind a document’s content. | underPageBackgroundColor |
| Unemphasized selected content background color | The selected content in a non-key window or view. | unemphasizedSelectedContentBackgroundColor |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | unemphasizedSelectedTextBackgroundColor |
| Unemphasized selected text color | Selected text in a non-key window or view. | unemphasizedSelectedTextColor |
| Window background color | The background of a window. | windowBackgroundColor |
| Window frame text color | The text in the window’s title bar area. | windowFrameTextColor |

### Accent color

- iOS, iPadOS, visionOS: the app accent color tints prominent buttons, selected tabs, sidebar icons, and similar emphasis. Keep it to one or two prominent elements per view and reserve it for primary actions and status.
- macOS: the app accent applies only when the person's system setting is "multicolor"; otherwise the system replaces it with the person's chosen accent everywhere except fixed-color sidebar icons.
- On Liquid Glass, apply color to the background of the one primary action, not to the symbols or text of many controls. Prefer monochrome bars when the content is colorful.

### Dark Mode

Both appearances are mandatory (iOS, iPadOS, macOS, tvOS). Do not add an in-app appearance switch. Dark palettes use dimmer backgrounds and brighter foregrounds and are not simple inversions. Soften white image backgrounds in Dark Mode. Test with Increase Contrast and Reduce Transparency on, separately and together.

## 4. Materials (source: [Materials](../references/foundations/materials.md))

| Material | Where | Notes |
|---|---|---|
| Liquid Glass, regular | Controls and navigation layer: tab bars, toolbars, sidebars, alerts, popovers | Default. Blurs and adjusts luminosity of what is beneath for legibility. |
| Liquid Glass, clear | Controls floating over rich media (photos, video) | Highly translucent. Add a dark dimming layer at 35% opacity over bright content; none needed over dark content or with AVKit controls. |
| Standard materials: ultraThin, thin, regular (default), thick | Content layer backgrounds and grouping (iOS, iPadOS) | Thicker = more contrast for small text; thinner = more context. Use vibrant label colors on top; avoid quaternary on thin and ultraThin. |
| macOS vibrancy and blending | Sidebars, content layer | Choose by semantic use, not by the color it imparts. |
| visionOS glass | Window background | Not modifiable; keep it. Buttons on glass use the thin material; buttons floating in space use glass. |

Rules: never use Liquid Glass in the content layer (exception: a slider or toggle takes on glass while active); apply custom glass effects sparingly; let standard components pick up glass automatically; use a scroll edge effect instead of a solid bar background; extend full-bleed content under bars and sidebars.

## 5. Icons and images

### App icon specifications (source: [App icons](../references/foundations/app-icons.md))

| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

Color spaces: sRGB, Gray Gamma 2.2, Display P3 (not visionOS). Deliver layered icons through Icon Composer (iOS, iPadOS, macOS, watchOS) or an Xcode image stack (tvOS 2 to 5 layers, visionOS background plus 1 or 2 layers). Provide square unmasked layers; the system applies corner rounding or the circular mask. No system effects baked in, no text unless essential, no photos, no replicas of Apple hardware, consistent design across platforms, dark and tinted variants kept consistent with the default. watchOS: avoid black backgrounds.

### macOS document icons (source: [Icons](../references/foundations/icons.md))

Background fill sizes: 512, 256, 128, 32, 16 px at 1x (double at 2x). Center image sizes: 256, 128, 32, 16 px at 1x. Keep about a 10 percent margin and most of the image within 80 percent of the canvas. Avoid important content in the top-right corner (the folded corner).

### Interface icons and SF Symbols

- Prefer SF Symbols; they come in 9 weights matching SF text weights and 3 scales (small, medium, large) relative to cap height.
- Rendering modes: monochrome, hierarchical, palette, multicolor; gradients in SF Symbols 7. Variable color communicates change, not depth.
- Variants: outline for toolbars and lists beside text; fill for iOS tab bars, swipe actions, and accent-colored selection; enclosed shapes improve legibility at small sizes.
- Custom interface icons: vector (PDF or SVG), consistent stroke weight and perspective, optically centered, with alternative text labels. Never use SF Symbols in app icons or logos.

### Standard action symbols (source: Icons)

**Editing**: Cut = `scissors`, Copy = `document.on.document`, Paste = `document.on.clipboard`, Done = `checkmark`, Cancel = `xmark`, Delete = `trash`, Undo = `arrow.uturn.backward`, Redo = `arrow.uturn.forward`, Compose = `square.and.pencil`, Duplicate = `plus.square.on.square`, Rename = `pencil`, Move to = `folder`, Attach = `paperclip`, Add = `plus`, More = `ellipsis`

**Selection**: Select = `checkmark.circle`, Deselect = `xmark`, Delete = `trash`

**Text formatting**: Superscript = `textformat.superscript`, Subscript = `textformat.subscript`, Bold = `bold`, Italic = `italic`, Underline = `underline`, ​​Align Left = `text.alignleft`, Center = `text.aligncenter`, Justified = `text.justify`, Align Right = `text.alignright`

**Search**: Search = `magnifyingglass`, Find = `text.page.badge.magnifyingglass`, Filter = `line.3.horizontal.decrease`

**Sharing and exporting**: Share = `square.and.arrow.up`, Print = `printer`

**Users and accounts**: Account = `person.crop.circle`

**Ratings**: Dislike = `hand.thumbsdown`, Like = `hand.thumbsup`

**Layer ordering**: Bring to Front = `square.3.layers.3d.top.filled`, Send to Back = `square.3.layers.3d.bottom.filled`, Bring Forward = `square.2.layers.3d.top.filled`, Send Backward = `square.2.layers.3d.bottom.filled`

**Other**: Alarm = `alarm`, Archive = `archivebox`, Calendar = `calendar`

### Bitmap images

Provide the scale factors each platform needs: iOS @2x and @3x; iPadOS and watchOS @2x; macOS and tvOS @1x and @2x; visionOS @2x or higher, embed a color profile, prefer vector for 2D art, avoid transparency to keep files small, use autoscaling PDFs where possible ([Images](../references/foundations/images.md)).

## 6. Input targets and gestures

### Standard gestures (source: [Gestures](../references/inputs/gestures.md))

| Gesture | Supported in | Common action |
|---|---|---|
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Activate a control; select an item. |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal actions and controls; dismiss views; scroll. |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Move a UI element. |
| Touch (or pinch) and hold | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal additional controls or functionality. |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Zoom in; zoom out if already zoomed in; open an item on a Mac with a touch display; perform a primary action on Apple Watch Series 9 and later and Apple Watch Ultra 2 and later. |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | Zoom a view; magnify content. |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate a selected item. |

iOS and iPadOS extras: three-finger swipe left/right = undo/redo; three-finger pinch in/out = copy/paste; four-finger swipe (iPadOS) = switch apps; shake = undo/redo.

### Essential keyboard shortcuts (source: [Keyboards](../references/inputs/keyboards.md))

Command-N new, Command-O open, Command-S save, Shift-Command-S duplicate or Save As, Command-W close window, Command-P print, Command-Q quit, Command-Z undo, Shift-Command-Z redo, Command-X/C/V cut/copy/paste, Option-Shift-Command-V paste and match style, Command-A select all, Command-F find, Command-G find next, Command-Comma settings, Command-Question mark help, Command-M minimize, Option-Command-T show/hide toolbar, Control-Command-F full screen, Esc cancel, Command-Period cancel operation, Command-B/I/U bold/italic/underline. Never repurpose these.

## 7. Motion

- Only purposeful motion; make it optional (respect Reduce Motion) and cancelable; keep feedback animations brief and precise; avoid animating frequent interactions beyond what the system already does.
- Games: aim for a consistent 30 to 60 fps.
- visionOS: avoid motion at the edges of the field of view; avoid sustained oscillation near 0.2 Hz; prefer fades over moving large objects; do not rotate the virtual world. ([Motion](../references/foundations/motion.md))

## 8. Quick token sheet

| Token | Value | Source |
|---|---|---|
| Touch target | 44x44 pt (iOS, iPadOS, watchOS); 60x60 pt visionOS; 28x28 pt macOS default; 66x66 pt tvOS | Accessibility, Buttons |
| Body text | 17 pt iOS/iPadOS/visionOS, 13 pt macOS, 29 pt tvOS, 16 pt watchOS | Typography |
| Minimum text | 11 / 10 / 23 / 12 / 12 pt (iOS-iPadOS / macOS / tvOS / visionOS / watchOS) | Typography |
| Body leading | 22 pt iOS Large, 16 pt macOS, 36 pt tvOS, 18.5 pt watchOS Large | Typography |
| Contrast | 4.5:1 minimum (text up to 17 pt), 3:1 at 18 pt or bold; 7:1 goal for custom colors | Accessibility, Dark Mode |
| Text enlargement | 200% (140% watchOS) | Accessibility |
| Control padding | about 12 pt with bezel, about 24 pt without | Accessibility |
| tvOS safe area | 60 pt top/bottom, 80 pt sides | Layout |
| tvOS tab bar | 68 pt tall, 46 pt from top | Tab bars |
| visionOS window | 1280x720 pt default, about 2 m away | Windows |
| visionOS button spacing | centers at least 60 pt apart | Buttons |
| Clear glass dimming | 35% dark layer over bright content | Materials |
| App icon canvas | 1024 px (1088 px watchOS, 800x480 px tvOS) | App icons |
| Toolbar title | under 15 characters | Toolbars |
| Toolbar groups | at most three | Toolbars |
| Prominent buttons per view | one or two | Buttons |
| Action sheet buttons (watchOS) | at most four including Cancel | Action sheets |
| Submenu | one level deep, about five items max | Menus |
| Sidebar hierarchy | at most two levels | Sidebars |
| Game initial download | 30 minutes or less | Designing for games |
