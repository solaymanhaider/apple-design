# What Apple's diagrams show

Apple's guidelines carry 1,509 images. Their text descriptions are already in `references/`; this file adds what a
person sees when looking at the 411 diagrams, anatomy illustrations, and specification figures that carry layout or
measurement information. Every entry was written while viewing the image. The page text remains the rule; these
notes describe Apple's illustrated intent, so an agent can reproduce the arrangement, not just the words.

Entries are grouped by HIG page in alphabetical order and name the section the image sits in.

## Accessibility ([reference](../references/foundations/accessibility.md))

- **Vision:** insufficient contrast example is dark-blue text on a bright blue capsule; sufficient contrast is white text on a deep blue capsule. The default iOS red and the accessible (Increase Contrast) red are shown side by side on light and dark halves: the accessible red is darker on light and lighter on dark.
- **Mobility:** insufficient padding shows three media buttons (previous, play, next) touching; sufficient padding shows each button's hit region as a larger box with space between regions. "Edit and tap to delete" shows red minus buttons on each row in edit mode; "Swipe to delete" shows a red Delete action revealed at the trailing edge of a row.

## Activity rings ([reference](../references/components/status/activity-rings.md))

- **Best practices:** Move ring R250 G17 B79, Exercise ring R166 G255 B0, Stand ring R0 G255 B246. iOS Summary with Apple Watch paired shows three rings (Move 300/300 CAL, Exercise 30/30 MIN, Stand 12/12 HRS); with no watch paired, only the Move ring plus Steps and Distance.

## Alerts ([reference](../references/components/presentation/alerts.md))

- **Anatomy:** iOS alert is a centered card with a bold title, a message, and two capsule buttons side by side (Secondary gray leading, Primary accent-filled trailing). macOS alert is a small centered sheet with the buttons stacked vertically, Primary (blue) on top, Secondary below. tvOS alert is a glass card over the content with Secondary and Primary side by side. visionOS alert has a blue icon badge above the title and stacked text buttons (Primary, then Secondary). watchOS alert is full screen with the title and message centered and full-width capsule buttons stacked, Primary (green) above Secondary (purple-pink gradient).

## App icons ([reference](../references/foundations/app-icons.md))

- Icon Composer shows layer groups in a sidebar (orange, blue, red, green, yellow, purple, pink, lime), a 1024 pt canvas, and inspector controls for Opacity, Blend Mode, Fill, Liquid Glass effects, Composition visibility, and Layout. The icon grid for iOS, iPadOS, and macOS is a rounded square with concentric circles and diagonals; tvOS is a landscape rectangle with the same guides; visionOS and watchOS use a circular grid. Podcasts and Home icons illustrate filled, overlapping, layered shapes with depth.

## Apple In-App Purchase ([reference](../references/technologies/apple-in-app-purchase.md))

- **watchOS:** one purchase option per full-width button ("$4.99 / Month", "$29.99 / Year") with a savings line beneath ("12 months at $2.49/mo. Save 50%").

## Apple Pay ([reference](../references/technologies/apple-pay.md))

- correct offering is a green checkmark circle; incorrect is a gray X circle. Payment sheet error messaging: in the sheet a row shows red text ("Update Shipping Address" in the Ship to row); in the custom detail view an invalid item shows a red message under its name ("Unknown postal code for your country.") while the Pay total stays visible. Fixed subscription shows the per-period price with "Starting Today" and an end date; variable subscription shows "Amount Pending" as the total; "Billing Details" row carries the merchant name, the localized billing agreement text, and a schedule line ("Recurring, Starting June 8, $9.99 per month for 6 months"); a free trial adds "3-month free trial, Free, 3 Months" above it; no payment required at authorization shows $0.00.
- **Apple Pay button:** black buttons with white text and the Apple Pay mark: Buy with, Pay with, Check Out with, Continue with, Book with, Donate with, Subscribe with, Reload with, Add Money with, Top Up with, Order with, Rent with, Support with.
- **Apple Pay button (continued):** Contribute with, Tip with, the plain Apple Pay mark, and Set Up Apple Pay.
- **Button size and position:** the Apple Pay button is correct when it is the same size as the custom Add to Cart button, placed above it or on its trailing side; wrong when it is smaller, or placed below, or on the leading side. Corner radius must match the custom button: minimum (slightly rounded), default (rounded rectangle), maximum (capsule). Minimum size: 30 pt tall; 100 pt wide for the logo-only button, 140 pt wide for a text button; margins at least 1/10 of the button height on every side.

## Apple Pencil and Scribble ([reference](../references/inputs/apple-pencil-and-scribble.md))

- diagrams show altitude (pencil angle to the surface, a blue fan of marks), pressure (stroke thickens with pressure, a blue wedge), and azimuth (the direction the pencil points around a circle of ticks).

## Augmented reality ([reference](../references/technologies/augmented-reality.md))

- app-specific placement indicator is a reticle of concentric arcs with corner brackets; direct manipulation shows a hand rotating a cube by dragging; indirect controls are undo and redo style rotate-left and rotate-right buttons beneath the object; rotation limited to a single vertical axis; object labels in the camera view are small black pills with a chevron ("Table #153 >", "Chair #225 >") connected to the object by a thin leader line; the detail view shows the object, name, price, dimensions, and a black "Purchase" capsule; sufficient lighting is a bright room, insufficient is a dim one. The AR glyph is a wire cube with bold corner marks; the AR badge is a rounded rectangle with the glyph plus "AR"; the glyph-only badge is a rounded square.

## Buttons ([reference](../references/components/menus-and-actions/buttons.md))

- **iOS, iPadOS:** the Checkout button example is a light gray capsule with blue text (the default, non-prominent style). visionOS button states: idle (translucent circle), hover (lighter fill), selected (white fill with black glyph), unavailable (dimmed fill and glyph).

## Camera Control ([reference](../references/inputs/camera-control.md))

- the overlay appears centered at the top of the viewfinder beside the Dynamic Island with five symbols (exposure, f-stop, zoom, aperture, tone) and a yellow uppercase label beneath ("ZOOM"); slider control shows a tick ruler with a yellow indicator and "1x"; picker control shows four dots with the selected one as a yellow bar and "STARK B&W"; zoom factor control shows the ruler with "1x"; exposure bias control shows a ruler with "0 EV".

## CareKit ([reference](../references/technologies/carekit.md))

- tasks view uses a week strip of day rings (completed days show a checkmark), a date header ("June 6"), and task cards with title, time range, instruction, and a full-width "Completed" button with a checkmark; contact cards show avatar, name, specialty, description, Call / Message / Email buttons, and an address row with a directions arrow; charts come in bar, scatter, and line styles with dashed grid lines, weekday axis, today highlighted as a filled circle, and a legend chip; contact views have simple (name, specialty, chevron) and detailed variants.

## Charts ([reference](../references/components/content/charts.md))

- **Anatomy:** labeled parts are grid line, plot area, mark, axis, tick, and axis value label (tick label); the y axis runs 0, 50, 100 and x shows 9, 10, 11, 12 PM.
- **Axes:** a Health-style bar chart puts a D / W / M / 6M / Y segmented control at the top, then an "AVERAGE" caption, a large value with unit ("1,577 steps"), the date range, and a bar chart with dashed horizontal grid lines and right-aligned y labels; the weekly range uses day names (Sat to Fri) and a 0 to 6,000 axis; the monthly range uses date ticks (22, 29, 6, 13) and a 0 to 10,000 axis.

## Color ([reference](../references/foundations/color.md))

- **Best practices:** with Increase Contrast on, the yellow accent of the prominent Done button becomes a darker mustard in light mode and a brighter yellow in dark mode, the red Delete menu item becomes deeper red, and glass control outlines get stronger.

## Complications ([reference](../references/components/system-experiences/complications.md))

- **Modular large:** columns (three label-value rows, labels colored), standard body (colored header line plus two body lines), table (header plus two rows of number and name), tall body (small colored header plus one large line). Extra large: ring image, ring text, simple image, simple text, stack image, stack text at larger scale.
- **Circular:** closed gauge image (full ring in one color with a symbol inside), closed gauge text (ring with a large number), open gauge image (gradient arc with a value and a symbol beneath), open gauge text (arc with value and a unit label such as AQI), open gauge range (arc with value and the two range endpoints in matching colors), image (a circular image), stack image (symbol above a value), stack text (two short lines, the second colored). Corner: circular image, gauge image (arc plus a symbol and a curved value like 14:59), gauge text (arc with endpoint labels and a large value), stack text (two curved lines, the second in the accent color), text image (curved timer text plus a symbol). Inline: flat (one line of text "LON 6:09"), ring image, ring text, square (small image), large flat ("11:00AM PHOTO SHOOT"). Rectangular: standard body (colored header line, two body lines), text gauge (header with symbol, body line, full-width progress bar), large image (header plus chart). Circular small and Modular small: ring image, ring text, simple image, simple text, stack image, stack text; Modular small also has columns text (two label-value rows). Modular large: tall body (colored weekday above a large date). Extra large: ring image, ring text, simple image, simple text, stack image, stack text at larger scale. Rings use a dim track with a bright progress arc; stacked layouts put the symbol above the value.
- **Modular large:** columns (three colored label rows with white values: CAL 396/660, MIN 13/30, HOUR 3/12), standard body (colored header "Cupertino, CA", two body lines), table (colored header "Final Score", two rows of number and name), tall body (colored weekday above a large date).

## Controls ([reference](../references/components/system-experiences/controls.md))

- **Anatomy:** a control is a capsule with a circular symbol image on the leading side, then a title line and a value (detail) line; in Control Center a toggle control is a circle, white-filled with a colored symbol when on, dark translucent with a white symbol when off; tinted on state shows the symbol in its tint color on white; the Dynamic Island shows a control performed from the Action button as a compact pill with symbol and state text ("Silent").
- **Anatomy:** a control is a capsule with a circular symbol image on the leading side, then a Title line with a Value (detail) line beneath it.
- **Anatomy:** in Control Center a toggle control is a circle; on (Wi-Fi, AirDrop) is a filled blue circle with a white symbol, off (airplane) is a dark translucent circle; the ringer-silenced toggle is a white circle with a red symbol. On the Lock Screen the two controls sit in the bottom corners (flashlight off is dark, silent on is white with red). Performed from the Action button, the Dynamic Island shows a compact pill with the symbol on the leading side and the state text ("Silent") on the trailing side. Nontinted toggle off: translucent glass circle with a white symbol; tinted toggle on: white circle with the symbol in the tint color (yellow bulb). A control with no information hidden shows a capsule with the symbol, a Title line and a Detail line.

## Dark Mode ([reference](../references/foundations/dark-mode.md))

- **iOS, iPadOS:** label hierarchy at four levels (label, secondaryLabel, tertiaryLabel, quaternaryLabel) on base (black) and elevated (dark gray) backgrounds in dark mode, and on white in light mode; each level is progressively more transparent.
- system blue, green, indigo, and purple are brighter in the dark appearance; an outline illustration works on a light background; primary label is black on white in light, secondary label is light gray on black in dark.
- Stocks is an example of a dark-only app; label hierarchy shows label, secondaryLabel, tertiaryLabel, quaternaryLabel on base black, elevated dark gray, and light white backgrounds, each level more transparent than the last.

## Designing for iPhone Duo ([reference](../references/getting-started/designing-for-iphone-duo.md))

- **Anatomy:** outer display is a tall narrow screen with the hinge along one long edge and the camera in a top corner; the inner display is a wide screen with the hinge running vertically down the center and the camera at the top of the right half. Six poses: closed, tent (landscape with a kickstand angle), fully open landscape, partially folded book, fully open portrait, and laptop-style with a folded base. Reserved regions: outer camera region (always), inner camera region (when active), folding region (vertical band at center when partially open).
- **Arrangement views:** split arrangement divides the inner display into primary (left) and secondary (right) halves; overlay arrangement shows the primary view as a rounded card floating centered over the full-screen secondary view. Notes on the inner display: sidebar list on the left half, note on the right half, toolbar buttons stacked vertically along the right edge, search field at the bottom of the left pane.
- **Anatomy:** the outer display is a tall screen with the hinge along one long edge and the camera in the top trailing corner; the inner display is a wide screen with the hinge running vertically down the center and the camera in the top of the right half. Six poses: closed, tented landscape, fully open landscape, partially folded (book), fully open portrait, and laptop-style with a folded base. Reserved regions: outer camera region (always present), inner camera region (when the camera is active), and the folding region (a vertical band at the center when partially open). Notes on the inner display: note list in the left half, note content in the right half, toolbar buttons stacked vertically along the right edge, search at the bottom of the list; when the inner camera activates, the right pane's content shifts away from it. Split arrangement divides the inner display into primary (left) and secondary (right) halves; overlay arrangement shows the primary view as a rounded card centered over the full-screen secondary view.

## Digital Crown ([reference](../references/inputs/digital-crown.md))

- shown on the side of Apple Vision Pro (pressed with a finger) and on Apple Watch (a red-ringed crown with the Sleep app behind). eyes: a square button versus a circular button, used to show that rounded shapes are easier to look at.

## Game Center ([reference](../references/technologies/game-center.md))

- Apple's Game Center screens use a dashboard header (game icon and name, large title), a two-column summary (a big number with a caption, friends' avatars with a caption), then sections (Completed, Ranked, Invites, Active); achievement art is circular with the completion date curved above it; leaderboard detail has Play (white, filled) and Challenge (translucent) buttons and a Friends/Global segmented filter; multiplayer level cards carry a "Multiplayer" badge and a player count ("2 to 4 Players") and party code.
- Apple's templates use a translucent dark blue sheet with a back button, game icon and name, large page title (Achievements, Leaderboards, Challenges, Multiplayer), a two-column summary (a large number such as 15/45 Total Completed, and friend avatars "You and 2 friends"), then sections (Completed, Ranked, Invites, Active). Achievement art is circular with the completion date curved above; the detail view has a Share button, title, description, and a "Players who have this" list. Leaderboard detail has white Play and translucent Challenge buttons and a Friends / Global segmented filter with a filter button; rows show rank, avatar, handle, name, and score. Challenge detail shows participants' avatars with rank badges ("3RD"), the title, time remaining ("23h 59m left"), and Play plus Add Players buttons. Multiplayer cards carry a "Multiplayer" badge, level name, and "2 to 4 Players"; the detail shows a party code and "Invite Players" with a Share Link button and a Friends & Contacts search field.

## Gauges ([reference](../references/components/status/gauges.md))

- **macOS:** a level indicator gauge is a horizontal bar split into tiered colored segments (red, yellow, green) with the remaining track in gray.
- **macOS:** tiered level indicator is a bar split into red, yellow, green segments with the remaining track gray.

## Gestures ([reference](../references/inputs/gestures.md))

- **visionOS system overlays:** looking at the palm shows a small circular Home indicator above the hand in the Shared Space and in a Full Space; a game with virtual gloves can defer the indicator.
- **visionOS system overlays:** looking at an upturned palm shows a small circular Home indicator above the hand in the Shared Space and in a Full Space; a game with virtual astronaut gloves defers the indicator.

## HomeKit ([reference](../references/technologies/homekit.md))

- the HomeKit icon is an outlined house with a chimney and nested inner house shapes; allowed in black, white on black, or a single custom color.
- the HomeKit icon is an outlined house with a chimney and two nested inner houses, shown in black, white on black, or a single custom color (blue).

## Icons ([reference](../references/foundations/icons.md))

- **Document icons (macOS):** a document icon composites a background fill (full-bleed pattern or gradient), a center image (single simple shape), and a short uppercase term at the bottom ("PROJECT", "SCENE"); the system adds the folded corner.
- **Document icons:** an Xcode project document composites a blue background fill with the Xcode glyph, a thin inner border, and the term "PROJECT" at the bottom; a HEART document type uses a pink grid-and-heartbeat background fill, a red heart center image, and the term "HEART"; a SceneKit document uses a white page with the SceneKit badge and the term "SCENE"; the folded corner is drawn by the system.

## ID Verifier ([reference](../references/technologies/id-verifier.md))

- the Verify Age and Verify Identity buttons are black capsules with white title-case text, like Apple Pay buttons.
- Verify Age and Verify Identity are black full-width capsules with white title-case text.

## Images ([reference](../references/foundations/images.md))

- **Resolution:** the same 10 pt circle is 10x10 px at 1x, 20x20 px at 2x, 30x30 px at 3x.
- **Resolution:** a 10 pt circle is 10x10 px at 1x, 20x20 px at 2x, 30x30 px at 3x.

## iMessage apps and stickers ([reference](../references/technologies/imessage-apps-and-stickers.md))

- **Sticker sizes:** the sticker browser shows 4 stickers per row at Small, 3 per row at Regular, 2 per row at Large.
- **Sticker sizes:** the sticker drawer shows four per row at Small, three per row at Regular, two per row at Large.

## Immersive experiences ([reference](../references/foundations/immersive-experiences.md))

- a window in the Shared Space floats in front of the real room; with dimmed passthrough the surroundings darken around the window; mixed immersion places 3D objects (a chair, a camera on a tripod) among real furniture.
- a Shared Space window floats in the room; dimmed passthrough darkens the surroundings around the highlighted window; mixed immersion in a Full Space places virtual objects (a director's chair, a camera on a tripod, a lamp) among real furniture.
- **Immersion styles:** progressive immersion dims the real room around the app's environment; full immersion replaces the room with a 360-degree custom environment (gallery walls with paintings).

## Inclusion ([reference](../references/foundations/inclusion.md))

- **Gender identity:** gender-neutral people symbols are person.crop.circle, person.3.fill, and figure.wave.

## Labels ([reference](../references/components/layout-and-organization/labels.md))

- **watchOS:** date, time, and timer labels are shown as plain system text ("2/11/23", "2:14PM", "00:06.34") in a rounded dark container; the timer uses a light weight at a large size.
- **watchOS:** date and time labels ("2/11/23", "2:14PM") are plain text in a dark rounded container; the timer label ("00:06.34") uses a large light-weight monospaced-digit style.

## Layout ([reference](../references/foundations/layout.md))

- **Size classes:** compact width and compact height is a small landscape-phone rectangle; compact width and regular height is a tall portrait rectangle; regular width and compact height is a wide short rectangle; regular width and regular height fills most of the screen.
- **tvOS grids:** rows of equal-width landscape cards (two to nine columns), the focused card scales up with a shadow and a "Title" label beneath it; rows are separated by horizontal rules and partial cards peek in at the trailing edge.
- **Size classes:** compact width and compact height is a small landscape rectangle; compact width and regular height is tall and narrow; regular width and compact height is wide and short; regular width and regular height fills most of the display.
- **tvOS grids:** rows of equal landscape cards from two to nine columns; the focused card scales up with a shadow and a "Title" label beneath; rows are separated by thin rules; partial cards peek in at the trailing edge.

## Live Activities ([reference](../references/components/system-experiences/live-activities.md))

- **Dynamic Island layouts:** content keeps an even margin from the Dynamic Island edge; drawing a shape all the way to the edge or placing an icon too far inside both read as wrong; group content with an inset rounded shape, or separate it with a thin line; the compact view shows a leading icon and a trailing value ("8min") on either side of the sensor cutout. watchOS Smart Stack shows a default view ("From Delivery App" header, icon, value) or a custom card (title, status line, large accent value, circular progress badge).
- **Creating Live Activity layouts:** in the expanded Dynamic Island keep an even margin around content (icon top leading, name and rating top trailing, "3 items" and "Arriving in 8 minutes" below, a full-width capsule button "Contact Juan C." at the bottom); drawing a circle to the island's edge, placing an icon too far inside, or placing it too close to the edge all read as wrong; to group content use an inset rounded capsule, or a thin line above it; blurred text too far from the edge is wrong and close to the edge is right. The iPhone compact view shows the icon on the leading side and "8min" on the trailing side of the sensor. watchOS Smart Stack: the default view shows "From Delivery App", the icon, and "8 min"; the custom view shows the app name, "Arriving in", "8 min" in the accent color, and a circular progress ring around the icon.

## Maps ([reference](../references/technologies/maps.md))

- default map style is full color; muted style desaturates everything except markers; clustered points show a single orange marker with a count ("3"); zoomed in, each point of interest becomes an orange circular pin with a category symbol and a label below.
- default style is full color; muted style desaturates everything except the point-of-interest marker; a cluster shows one orange circle with a count ("3"); zoomed in, each point of interest is an orange circular pin with a category symbol and a label beneath ("Coffee Shop").

## Materials ([reference](../references/foundations/materials.md))

- **Liquid Glass:** on dark backgrounds the glass element looks like a dark translucent disc with a soft rim; on light backgrounds it blurs and brightens what is beneath. A label in systemGray3 on a thin material has poor contrast.
- **Liquid Glass:** on a dark starfield the glass disc looks like a dark lens with a bright rim; on a bright beach photo it blurs and lifts the colors beneath. A systemGray3 share symbol on a thin material over a bright gradient has poor contrast.

## Offering help ([reference](../references/patterns/offering-help.md))

- **Creating tips:** a TipKit tip is a rounded card with a bold "Tip Title", a one or two line description, and a close (x) button in the top trailing corner; the popover style adds an arrow pointing at the control, the annotation style sits inline with the content.
- **Creating tips:** a TipKit tip is a rounded card with a bold "Tip Title", a one or two line description, and a close (x) button in the top trailing corner; popover style adds a small arrow pointing at the control; annotation style sits inline with an arrow; hint style is an inline card with no arrow.

## Page controls ([reference](../references/components/presentation/page-controls.md))

- **watchOS:** the vertical page control is a column of dots on the trailing edge beside the Digital Crown, with the current page as an elongated pill; the horizontal page control is a row of dots centered at the bottom.
- **watchOS:** the vertical page control is a column of dots on the trailing edge beside the Digital Crown with the current page shown as an elongated pill; the horizontal page control is a row of dots centered at the bottom with the current page in white.

## Pointing devices ([reference](../references/inputs/pointing-devices.md))

- **Standard pointers and effects (iPadOS):** hit region extends 12 pt beyond a bezeled button on every side; 24 pt beyond a bezel-less symbol or text button on every side (the 12 and 24 figures are drawn on the diagrams). A custom pointer example shows a horizontal resize cursor on a handle with an annotation "w: 837 pt h: 1080 pt".
- **Pointers (macOS standard pointer set):** arrow; closed hand (grabbing); arrow with contextual menu; crosshair plus; arrow with gray X circle (disappearing item); arrow with green plus circle (copy); curved alias arrow; I-beam text insertion (vertical); open hand; arrow with not-allowed circle; pointing hand (link); horizontal bar with down arrow (resize down); left-right resize with one side inactive (gray); left-right resize; bar with left arrow; bar with left and right arrows (column resize); up-down with one side gray; up-down; diagonal resize pairs (up-right, down-right) with inactive variants; bar with right arrow; up-down with gray up; diagonal with gray; bar with up arrow; bar with up and down arrows (row resize); left-right with gray right; horizontal I-beam (vertical text insertion); zoom in (magnifier plus); zoom out (magnifier minus).
- **Standard pointers and effects (iPadOS):** the hit region extends 12 pt beyond a bezeled button on every side; 24 pt beyond a bezel-less symbol or text button on every side. A custom resize pointer shows a horizontal double arrow on a handle with an annotation "w: 837 pt  h: 1080 pt".
- **Pointers (macOS standard set):** arrow; closed hand (grabbing); arrow with a small menu rectangle (contextual menu); plus (crosshair); arrow with a gray X circle (disappearing item); arrow with a green plus circle (copy); curved alias arrow; vertical I-beam (text insertion); open hand; arrow with a gray not-allowed circle; pointing hand (link); horizontal bar with a down arrow (resize down); left-right resize with the left side gray (cannot move left); left-right resize; bar with a left arrow (resize left); bar with left and right arrows (column resize); up-down with the down side gray; up-down resize; diagonal pairs for up-right and down-right with inactive gray variants; bar with a right arrow (resize right); up-down with the up side gray; diagonal with the top-left gray.
- **Pointers (continued):** bar with an up arrow (resize up); bar with up and down arrows (row resize); left-right with the right side gray; horizontal I-beam (vertical text insertion); magnifier with plus (zoom in); magnifier with minus (zoom out).

## Progress indicators ([reference](../references/components/status/progress-indicators.md))

- progress bar is a thin rounded track with a blue fill; circular progress indicator is a thick ring with blue progress on a gray track; macOS activity indicator is the 8-spoke spinner; watchOS activity indicator is a ring of six dots of varying brightness; macOS indeterminate bar shows a blue segment with gradient edges that travels along the track; watchOS progress bar is white on gray, circular is a white ring.
- progress bar is a thin rounded track with a blue fill from the leading edge; circular progress indicator is a thick ring, blue progress on a light gray track; macOS activity indicator is an eight-spoke spinner; watchOS activity indicator is a ring of six dots of graded brightness; macOS indeterminate bar shows a blue segment with a soft leading gradient that travels along the track; watchOS bar is white on dark gray and the watchOS circular indicator is a white ring on a gray track.

## Right to left ([reference](../references/foundations/right-to-left.md))

- **Text alignment:** in LTR the text block and card content align to the left margin line; in RTL the same layout mirrors to the right margin line, and the image inside the card stays centered.
- Arabic paragraphs align to the right edge and Latin paragraphs to the left even inside an RTL layout (mixed alignment is shown as wrong for list items: keep one alignment per list). Western numerals (123) keep left-to-right digit order in Arabic and Hebrew text; Eastern Arabic numerals are used where the locale expects them. A rating row of stars counts 1 to 5 left to right in Latin and 5 to 1 (right to left) in Arabic and Hebrew. A volume slider mirrors in RTL: the loud speaker icon moves to the leading (right) side and the fill grows from the right. Directional SF Symbols (list bullets, book, scribble, window controls, battery) have mirrored RTL variants; text-bearing symbols (signature, text box, text cursor "A") have Latin, Hebrew, and Arabic variants; logos (Apple TV) and universal marks (checkmark) never flip.
- in LTR the text and card content align to the left margin line; in RTL they mirror to the right margin line and the image stays centered. Arabic paragraphs align right and Latin paragraphs align left even in an RTL layout; a right-aligned Latin paragraph in RTL is shown as the alternative. Lists keep one alignment for every row; a row that aligns left while the rest align right is marked as wrong (mixed alignment). Western Arabic numerals keep 1-2-3 order; Eastern Arabic numerals are used in Arabic where the locale expects them; "Order number 123456" keeps digit order in Latin, Hebrew, and Arabic. A five-star rating counts 1 to 5 left to right in Latin and 5 to 1 right to left in Arabic (Eastern numerals) and Hebrew. A volume slider mirrors in RTL: the loud speaker moves to the leading (right) side and the fill grows from the right. Directional symbols with RTL variants: list bullet, book, scribble, window with controls, battery. Text symbols with Latin, Hebrew, and Arabic variants: signature, text-and-image card, text cursor with a letter. Logos (Apple TV) and universal marks (checkmark) never flip.

## Scroll views ([reference](../references/components/presentation/scroll-views.md))

- **Scroll edge effects:** hard scroll edge effect shows a visible blurred band with a crisp bottom edge under the toolbar; soft scroll edge effect fades gradually into the content with no visible line.
- **Scroll edge effects:** the hard scroll edge effect is a blurred band with a crisp bottom edge under the toolbar; the soft effect fades gradually into the content with no visible line.

## Search fields ([reference](../references/components/navigation-and-search/search-fields.md))

- **Search as a tab:** the standard search tab is the trailing tab in the tab bar (magnifier plus "Search" label); the button appearance separates search into its own circular button next to the tab bar. Search in a bottom toolbar: a full-width search field between a menu button and a compose button; search in a top toolbar: a magnifier button grouped with More, next to a plus button. iPadOS and macOS search fields show suggestions in a dropdown under the field, with the typed prefix in bold and completions in gray (iPad) or a highlighted first row (Mac).
- standard search tab is the trailing tab (magnifier, "Search" label); button appearance separates search into its own circular button beside the tab bar; bottom toolbar search is a full-width field between a menu button and a compose button; top toolbar search is a magnifier grouped with More, next to a plus button. iPadOS suggestions drop down under the toolbar field with the typed prefix bold and completions gray; macOS suggestions list under the field with the first row highlighted in the accent color.

## Segmented controls ([reference](../references/components/selection-and-input/segmented-controls.md))

- single-choice style highlights one segment in the accent color (text alignment example); multiple-choice style lets several segments stay selected at once (bold, italic, underline on, strikethrough off).
- single choice highlights one segment in the accent color (text alignment); multiple choice can keep several segments selected at once (Bold, Italic, Underline on; Strikethrough off).

## SF Symbols ([reference](../references/foundations/sf-symbols.md))

- **Rendering modes:** hierarchical rendering gives the primary layer full opacity and secondary and tertiary layers reduced opacity (cloud, sun, rain example). Gradient fill adds a subtle vertical gradient to a solid symbol. Scales: small, medium, and large symbols align to the same text baseline and cap height next to the word "Add"; large is noticeably taller than cap height.
- **Design variants:** outline row versus fill row for heart, heart.slash, heart.circle, heart.square, heart.rectangle; localized variants exist for Latin, Arabic, Hebrew, Devanagari, Armenian, Chinese, Japanese, Korean.
- hierarchical rendering of cloud.sun.rain gives one layer full opacity and the others light gray (primary cloud, secondary sun, tertiary rain); a solid-fill sun versus a gradient-fill sun with a subtle vertical gradient; symbol scales small, medium, and large sit on the same cap height lines beside "Add", with large extending beyond the cap height; outline versus fill variants of heart, heart.slash, heart.circle, heart.square, heart.rectangle; localized variants for Latin, Arabic, Hebrew, Devanagari, Armenian, Chinese, Japanese, Korean across twelve symbols (character cards, textbox, a.circle, a.square, text bubbles, character, superscript, subscript, textformat.size, textbox, text cursor).

## Sheets ([reference](../references/components/presentation/sheets.md))

- **Anatomy:** the Notes format sheet is a nonmodal sheet; people can keep selecting text in the note above while the sheet stays open. iOS detents: large detent covers the screen from just below the status bar with a grabber and a Close (x) button at top leading; the medium detent rests at about half height with the same grabber and Close button.
- **Anatomy:** the Notes format sheet is nonmodal and people can still select text in the note while it is open. Large detent fills the screen from just below the status bar with a grabber and a Close (x) button at the top leading corner; medium detent rests at about half height with the same grabber and Close button.

## Sign in with Apple ([reference](../references/technologies/sign-in-with-apple.md))

- **Button size and corner radius:** black button with the Apple logo and "Sign in with Apple" in white; minimum corner radius (slight), default (rounded rectangle), maximum (capsule). Logo-only buttons: rounded rectangle mask, no mask (square), circular mask.
- black "Sign in with Apple" button with white Apple logo and text in minimum (slightly rounded), default (rounded rectangle), and maximum (capsule) corner radius; logo-only buttons use a rounded rectangle mask, no mask (square), or a circular mask.

## Sliders ([reference](../references/components/selection-and-input/sliders.md))

- **macOS:** linear slider with a round white knob, optional tick marks below the track; circular slider is a dial with a dot marker. watchOS discrete slider: minus and plus buttons on either side of a segmented level indicator.
- **macOS:** linear slider with a round white knob, with or without small tick marks beneath the track; circular slider is a white dial with a gray dot marker. watchOS discrete slider: minus and plus speaker buttons on either side of a segmented green level indicator.
- **watchOS:** continuous slider also uses minus and plus speaker buttons with a thin green level line between them.

## Snippets ([reference](../references/components/system-experiences/snippets.md))

- **Anatomy:** a snippet is a rounded card with the dialogue line at the top ("Dialogue"), a custom view beneath it with a maximum height of 400 pt, and Secondary (gray) and Primary (accent-filled) capsule buttons at the bottom.

## Tab bars ([reference](../references/components/navigation-and-search/tab-bars.md))

- **visionOS:** collapsed, the tab bar is a vertical capsule of symbols with the selected one in a lighter circle; expanded on gaze, it widens to show symbol plus "Label" rows with the selected and hovered rows highlighted.

## Tab views ([reference](../references/components/layout-and-organization/tab-views.md))

- **Anatomy (macOS):** a three-tab tabbed control (First, Second, Third) sits centered at the top of the window beside the traffic-light window controls, with the selected tab in a lighter capsule.

## Text fields ([reference](../references/components/selection-and-input/text-fields.md))

- **Best practices:** formatted fields show "Number: 100000.00" and "Currency: $100,000.00" right-aligned in bordered fields; clipped text cuts mid-word at the field edge, wrapped text grows the field to two lines, truncated text ends with an ellipsis.

## Toggles ([reference](../references/components/selection-and-input/toggles.md))

- iOS switches sit on the trailing edge of a list row with the title on the leading edge; off is a gray track with a white knob, on is a green track (standard) or the app tint such as indigo (custom); macOS checkbox states are on (blue rounded square with a white checkmark), off (light gray rounded square), mixed (blue with a white dash); radio buttons are a blue circle with a white dot when selected and a light gray circle when deselected.

## Toolbars ([reference](../references/components/menus-and-actions/toolbars.md))

- **visionOS:** a glass capsule with four text labels, the selected one in a lighter capsule. watchOS: top toolbar buttons sit in the top corners (info on the leading side, plus on the trailing side) with the time centered above a blue title; bottom toolbar buttons sit in the bottom corners (location, search) with the time at the top; a scrolling toolbar button is hidden above the list and revealed as a full-width green "Action" capsule under the title when people scroll up.

## Typography ([reference](../references/foundations/typography.md))

- **Supporting Dynamic Type:** the Mail message at the default size shows the toolbar, sender row with avatar, subject in bold, and body text at body size.

## Wallet ([reference](../references/technologies/wallet.md))

- a Lock Screen banner shows the pass icon on the leading side, the app name, a message ("Get ready for today's workout! Open your membership pass to badge in."), and the pass thumbnail on the trailing side; a Live Activity for an event ticket shows the ticket art, "Soccer Match", and Lvl / Row / Seat values; event tickets with a background image or a solid color both show the icon and name at the top leading, "ACCESS VIP" top trailing, uppercase small labels (EVENT, LOCATION, TIME, LEVEL, ROW, SEAT) with values beneath, a square thumbnail on the trailing side, and a barcode at the bottom; a boarding pass shows the primary logo (square mark plus "Airline" logo text, or a rectangular wordmark with no logo text) top leading and "AP 1042 JUN 8" top trailing, then city names above SFO and NRT with a plane between, times beneath, the passenger name, and status chips (GOLD MEMBER, ECONOMY, PREBOARD ELIGIBLE); the pass icon also appears at the bottom-leading corner of the QR code area in Wallet and in Lock Screen banners; pass detail rows offer actions such as "Go to Terminal I, Open in Maps" and "Track Luggage, Open in Find My"; a membership pass layout puts the logo and member number at the top, a QR code centered toward the bottom, and name and expiry at the bottom; the safe areas diagram marks the top-leading logo region, the top-trailing header field region, the central barcode region, and the whole bottom band as areas the background must keep clear; the order tracking dashboard is a sheet titled "Orders" with a Done button, a search field, and cards showing merchant, order time, a green status ("Ready for Pickup", "Arriving Tomorrow"), item summary, and item thumbnails.

## Widgets ([reference](../references/components/system-experiences/widgets.md))

- **Appearances:** a small Stocks widget in full color (black background, green ticker line and change), clear (translucent glass over the wallpaper with white text), tinted (the wallpaper tint color, purple, with white text), StandBy (black background, white and green), and StandBy in low light (everything rendered in red on black); the interactive Reminders widget shows a count, a red "Reminders" label, and a list of circles that fill red when tapped; StandBy in low light shows a red analog clock and red weather; a widget viewed from a distance shows only the album art and large "ALBUM NAME" and "Artist Name", while viewed nearby it adds the song list in small text.

## Windows ([reference](../references/components/presentation/windows.md))

- **macOS window states:** the inactive Finder window sits behind with gray controls, the main Notes window is in front with colored controls, and the Colors panel is the key window floating above it. visionOS: a window is drawn as a flat upright blue plane with a window bar beneath; a volume is a translucent cube with a solid floor and a window bar; a real window shows the "Hello World" glass panel floating in the room, a window with 3D content shows a satellite model extending in front of the glass with a back button, title, text, "View Orbits" button, and a segmented control at the bottom, and a volume shows a globe floating above a coffee table with a small ornament of controls beneath it.
