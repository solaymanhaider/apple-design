# Components guide

This guide condenses every component page in Apple's Human Interface Guidelines (HIG) into decision-oriented entries so an agent can pick the right component and build it correctly. Each entry keeps Apple's bold best-practice sentences as short imperative rules, preserves Apple's exact numbers, and points back to the full reference page under `../references/components/`. Platform availability comes from each page's `Platforms:` line. The "Web equivalent" line in each entry is a translation written for this skill, not Apple guidance; it suggests how to realize the same behavior with semantic HTML, ARIA and CSS while keeping Apple's rules.

How to use this guide:

1. Start with the "Choosing a component" table to map a need to a component and to see what people wrongly reach for.
2. Open the component entry, follow the "Use it when" and "Don't use it when" bullets, then implement the "Rules" list.
3. Check "Platform notes" for the platform you target and "Content/labels" for capitalization and wording.
4. Read the linked reference when you need the full page, images, tables, or developer links.

## Choosing a component

| Need | Use | Not |
|---|---|---|
| Navigate between top-level sections of an app | [Tab bars](../references/components/navigation-and-search/tab-bars.md) (iOS, iPadOS, tvOS, visionOS); [Sidebars](../references/components/navigation-and-search/sidebars.md) when the hierarchy is wide and space is regular | A segmented control or a toolbar; a tab bar is for navigation, not actions |
| Navigate top-level collections (folders, playlists) with lots of vertical space | [Sidebars](../references/components/navigation-and-search/sidebars.md) | A tab bar with a More tab; hiding the sidebar by default |
| Show multiple levels of hierarchy side by side | [Split views](../references/components/layout-and-organization/split-views.md) | Opening new windows; a split view in a compact iPhone layout |
| Switch between closely related panes of content in the same area (macOS) | [Tab views](../references/components/layout-and-organization/tab-views.md) | A pop-up button to switch tabs; more than six tabs |
| Switch between closely related subviews (iOS, iPadOS) | [Segmented controls](../references/components/selection-and-input/segmented-controls.md) | A tab bar for subviews; a tab view (not supported) |
| Present a scoped task that people finish before returning | [Sheets](../references/components/presentation/sheets.md) | An alert; a popover in a compact view; a sheet for prolonged multistep flows (use full screen or a window) |
| Show a critical interruption or confirm an uncommon destructive action | [Alerts](../references/components/presentation/alerts.md) | An alert for purely informative content; an alert at app launch; a notification for an error |
| Offer choices related to an action people just initiated | [Action sheets](../references/components/presentation/action-sheets.md) | An alert (no extra choices); a menu (people expect a menu only when they reveal it) |
| Show a small amount of transient info or controls anchored to an element (regular width) | [Popovers](../references/components/presentation/popovers.md) | A popover in a compact view (use a sheet); a popover to show a warning (use an alert) |
| Show supplementary controls that float above a document (macOS) | [Panels](../references/components/presentation/panels.md) | A sheet when people need to repeatedly provide input and observe results; a HUD without a media reason |
| Initiate an instantaneous action | [Buttons](../references/components/menus-and-actions/buttons.md) | A toggle, segmented control, or pop-up button, which are button-like but have distinct roles |
| Pick one of a few mutually exclusive options (compact) | [Pop-up buttons](../references/components/menus-and-actions/pop-up-buttons.md); [Segmented controls](../references/components/selection-and-input/segmented-controls.md) when all choices should stay visible; radio buttons on macOS via [Toggles](../references/components/selection-and-input/toggles.md) | A pull-down button (that is for actions); a picker for a short list (too much visual weight) |
| Pick one of many values, or a date or time | [Pickers](../references/components/selection-and-input/pickers.md) | A pull-down button for a long list; a picker for a very large set (use a list or table) |
| Offer commands or items directly related to a button's action | [Pull-down buttons](../references/components/menus-and-actions/pull-down-buttons.md) | A pop-up button for actions; hiding all of a view's primary actions in one pull-down button |
| Display commands relevant to a specific item without cluttering the UI | [Context menus](../references/components/menus-and-actions/context-menus.md) | Both a context menu and an edit menu on the same item; dimming unavailable items (hide them) |
| Edit, copy, look up, or translate selected content | [Edit menus](../references/components/menus-and-actions/edit-menus.md) | A custom menu that duplicates system edit commands; extra controls that duplicate edit menu items |
| Expose frequent commands, navigation, title, and search for a view | [Toolbars](../references/components/menus-and-actions/toolbars.md) | A tab bar for actions; a manually added overflow menu; many groups (aim for three max) |
| List every command an app supports (macOS, iPadOS) | [The menu bar](../references/components/menus-and-actions/the-menu-bar.md) | Hiding menu items instead of disabling them; the menu bar as the only place for a command on iPad |
| Share or act on content with system and app activities | [Activity views](../references/components/menus-and-actions/activity-views.md) via the Share button | A custom share flow; duplicate Print or Copy actions |
| Offer app actions from the Home Screen icon | [Home Screen quick actions](../references/components/menus-and-actions/home-screen-quick-actions.md) | Emoji as icons; more than four actions |
| Offer app actions from the Dock icon (macOS) | [Dock menus](../references/components/menus-and-actions/dock-menus.md) | Making a Dock menu the only place for a command |
| Present window-level controls near a visionOS window | [Ornaments](../references/components/menus-and-actions/ornaments.md) | A custom ornament to build a toolbar or tab bar (the system already does that) |
| Enter a short piece of text (name, email, password) | [Text fields](../references/components/selection-and-input/text-fields.md) | A text view for one short value; a plain field for a password (use a secure field) |
| Enter or display long, multiline, or styled text | [Text views](../references/components/content/text-views.md) | A label for editable text; a text field for long text |
| Display static text people can read but not edit | [Labels](../references/components/layout-and-organization/labels.md) | A text field for uneditable text; custom colors instead of the four system label colors |
| Combine free text entry with a list of suggestions (macOS) | [Combo boxes](../references/components/selection-and-input/combo-boxes.md) | A pop-up button when people need a custom value |
| Turn a setting on or off | [Toggles](../references/components/selection-and-input/toggles.md) | A switch outside a list row on iOS (use a toggle-style button); a toggle to choose from a list |
| Choose a value in a continuous range | [Sliders](../references/components/selection-and-input/sliders.md) | A slider for audio volume on iOS (use a volume view) |
| Nudge a value up or down by small increments | [Steppers](../references/components/selection-and-input/steppers.md) | A stepper alone for wide value ranges (pair with a text field) |
| Pick a color | [Color wells](../references/components/selection-and-input/color-wells.md) | A custom picker when the system one fits |
| Edit, drag, or paste an image (macOS) | [Image wells](../references/components/selection-and-input/image-wells.md) | An image view with ad hoc editing |
| Display an image | [Image views](../references/components/content/image-views.md) | An image view with tap handlers (use a button); an image view for an icon (use a symbol) |
| Enter a PIN or passcode (tvOS) | [Digit entry views](../references/components/selection-and-input/digit-entry-views.md) | A plain text field for sensitive digits |
| Search a collection of content | [Search fields](../references/components/navigation-and-search/search-fields.md) | A custom search UI; search that waits for Return when immediate results are possible |
| Enter multiple discrete values like recipients (macOS) | [Token fields](../references/components/navigation-and-search/token-fields.md) | A comma-separated text field |
| Show a file system path (macOS) | [Path controls](../references/components/navigation-and-search/path-controls.md) | A path control in a toolbar or status bar |
| Show progress of an operation | [Progress indicators](../references/components/status/progress-indicators.md) | An indeterminate spinner when duration is known; switching from circular to bar style |
| Show a value within a known range | [Gauges](../references/components/status/gauges.md) | A progress indicator for a static value |
| Show a star ranking (macOS) | [Rating indicators](../references/components/status/rating-indicators.md) | Custom symbols that nobody associates with ranking |
| Show Move, Exercise, and Stand progress | [Activity rings](../references/components/status/activity-rings.md) | Activity rings for any other data, decoration, or branding |
| Show hierarchical data | [Outline views](../references/components/layout-and-organization/outline-views.md) (macOS); [Disclosure controls](../references/components/layout-and-organization/disclosure-controls.md); [Column views](../references/components/layout-and-organization/column-views.md) for deep hierarchies (macOS) | A flat table for hierarchical data; nested boxes |
| Show tabular data or scannable text rows | [Lists and tables](../references/components/layout-and-organization/lists-and-tables.md) | A collection for text; an index next to trailing disclosure indicators |
| Show a grid of visual items | [Collections](../references/components/layout-and-organization/collections.md) | A collection for text; a custom layout that draws attention to itself |
| Group related controls visually | [Boxes](../references/components/layout-and-organization/boxes.md) | A box nearly as large as its container; nested boxes |
| Show focusable media groups on Apple TV | [Lockups](../references/components/layout-and-organization/lockups.md) | Inconsistent lockup sizes in a row |
| Let people move through content larger than the view | [Scroll views](../references/components/presentation/scroll-views.md) | Nested scroll views with the same orientation |
| Indicate position in an ordered set of pages | [Page controls](../references/components/presentation/page-controls.md) | A page control for hierarchical or nonsequential pages; more than about 10 dots |
| Present an app's content in a resizable container | [Windows](../references/components/presentation/windows.md) | Custom window frames or controls; opening new windows by default |
| Embed web content | [Web views](../references/components/content/web-views.md) | A web view that tries to be a browser |
| Visualize data | [Charts](../references/components/content/charts.md) | Color alone to distinguish series; requiring interaction to reveal critical info |
| Show info at a glance outside the app | [Widgets](../references/components/system-experiences/widgets.md); [Complications](../references/components/system-experiences/complications.md) (watchOS) | A widget that only replicates the app icon; static content |
| Track an ongoing event with frequent updates | [Live Activities](../references/components/system-experiences/live-activities.md) | Repeated notifications; a widget for real-time data |
| Tell people about timely, high-value info | [Notifications](../references/components/system-experiences/notifications.md) | A notification for an error (use an alert); multiple notifications for the same thing |
| Give quick access to a feature from Control Center, Lock Screen, or Action button | [Controls](../references/components/system-experiences/controls.md) | A control that merely launches the app |
| Expose key tasks to Siri, Spotlight, and Shortcuts | [App Shortcuts](../references/components/system-experiences/app-shortcuts.md) | More than 10 App Shortcuts; complex voice phrases |
| Show a result or confirmation for a Siri or App Shortcut action | [Snippets](../references/components/system-experiences/snippets.md) | Repeating the spoken dialogue in the view; views taller than 400 pt |
| Manage the device status area (iOS, iPadOS) | [Status bars](../references/components/system-experiences/status-bars.md) | Permanently hiding the status bar |
| Showcase content on the Apple TV Home Screen | [Top Shelf](../references/components/system-experiences/top-shelf.md) | Ads or prices; implying interactivity in a static image |
| Promote complications through a shareable watch face | [Watch faces](../references/components/system-experiences/watch-faces.md) | Watch faces that only work on newer devices with no fallback |

---

## Content

### Charts
- **What it is:** Organize data in a chart to communicate information with clarity and visual appeal.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You want to highlight a few key pieces of information in a dataset so people can gain insights and make decisions (for example weather effects, stock trends, fitness progress).
  - People need to compare categories (bar), see change over time (bar or line), or inspect individual values and outliers (point).
- **Don't use it when / use instead:**
  - You just need to show a value within a range; use [Gauges](../references/components/status/gauges.md).
  - You need to show an operation's progress; use [Progress indicators](../references/components/status/progress-indicators.md).
  - You need a scannable table of exact values; use [Lists and tables](../references/components/layout-and-organization/lists-and-tables.md).
- **Rules:**
  - Choose a mark type based on the information you want to communicate about the data (bar, line, point).
  - Consider combining mark types when it adds clarity (for example points on top of a line).
  - Use a fixed or dynamic axis range depending on the meaning of your chart; a battery chart is fixed at 0% to 100%, a steps chart is dynamic.
  - Define the value of the lower bound based on mark type and chart usage; bars usually start at zero, heart rate charts should not.
  - Prefer familiar sequences of values in the tick and grid-line labels (0, 5, 10, not 1, 6, 11).
  - Tailor the appearance of grid lines and labels to a chart's use cases; too many grid lines overwhelm, too few make estimation hard.
  - Write descriptions that help people understand what a chart does before they view it.
  - Summarize the main message of your chart in a title and subtitle so people can grasp it quickly.
  - Establish a consistent visual hierarchy; the data is most prominent, descriptions and axes provide context.
  - In a compact environment, maximize the width of the plot area; keep vertical axis labels short, describe units in the title, and consider placing a long axis label inside the plot area.
  - Make every chart in your app accessible; support VoiceOver and consider Audio Graphs.
  - Let people interact with the data when it makes sense, but don't require interaction to reveal critical information.
  - Make it easy for everyone to interact with a chart; consider expanding the hit target to the entire plot area so people can scrub.
  - Make an interactive chart easy to navigate with keyboard commands (including full keyboard access) or Switch Control; specify a logical path or let people move among subsets of values.
  - Help people notice important changes in a chart; animate changes but also highlight them in other ways for VoiceOver users and people who turn off animations.
  - Align a chart with surrounding interface elements, for example by aligning the leading edge with other views and displaying grid-line labels on the trailing side.
  - Avoid relying solely on color to differentiate data; supplement color with shapes or patterns.
  - Aid comprehension by adding visual separation between contiguous areas of color (for example a narrow gap between stacked segments).
  - Consider using Audio Graphs to give VoiceOver users more information; otherwise describe the chart type, each axis, and the axis bounds.
  - Write accessibility labels that support the purpose of your chart; a chart often needs a label for each important or interactive element.
  - Hide visible text labels for axes and ticks from assistive technologies; VoiceOver users get values through accessibility labels and Audio Graphs.
- **Platform notes:**
  - iOS, iPadOS, macOS, tvOS, visionOS: No additional considerations.
  - watchOS: In general, avoid requiring complex chart interactions; prefer glanceable information and simple interactions, and use a companion app on another platform for details.
- **Content/labels:** Accessibility labels: prioritize clarity and comprehensiveness; avoid subjective terms like rapidly, gradually, almost; avoid ambiguous formats and abbreviations ("June 6" not "6/6", "60 minutes" not "60m"); describe what details represent, not what they look like; be consistent when referring to a specific axis.
- **APIs:** Swift Charts, `Chart3D` (SwiftUI); `accessibilityRespondsToUserInteraction(_:)` (SwiftUI); `UIAccessibility.Notification` (UIKit); `NSAccessibility.Notification` (AppKit).
- **Web equivalent (translation, not Apple guidance):** Render with inline `<svg>` or `<canvas>` wrapped in a `<figure>` with `<figcaption>` carrying the title and summary; give the figure `role="img"` with a descriptive `aria-label` or provide a data `<table>` alternative; make the whole plot area the pointer and keyboard target; never encode series by color alone.
- **Source:** [reference](../references/components/content/charts.md)

### Image views
- **What it is:** An image view displays a single image, or in some cases an animated sequence of images, on a transparent or opaque background.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - The primary purpose of the view is simply to display an image.
  - You need to stretch, scale, size to fit, or pin an image to a specific location.
- **Don't use it when / use instead:**
  - The image should be interactive; configure a system-provided [button](../references/components/menus-and-actions/buttons.md) to display the image instead of adding button behaviors to an image view.
  - You want to display an icon; consider an SF Symbol or interface icon instead.
  - People need to edit, paste, drag, or delete the image on macOS; use an [image well](../references/components/selection-and-input/image-wells.md).
- **Rules:**
  - Use an image view when the primary purpose of the view is simply to display an image.
  - If you want to display an icon in your interface, consider using a symbol or interface icon instead of an image view.
  - Take care when overlaying text on images; ensure contrast and consider a text shadow or background layer.
  - Aim to use a consistent size for all images in an animated sequence; prescale images to fit the view so the system doesn't have to scale.
  - Image views are typically not interactive.
- **Platform notes:**
  - iOS, iPadOS: No additional considerations.
  - macOS: If your app needs an editable image view, use an image well. Use an image button instead of an image view to make a clickable image.
  - tvOS: Many images combine multiple layers with transparency to create depth (see Layered images).
  - visionOS: Windows can display 2D and stereoscopic images and spatial photos in image views; with RealityKit you can display images next to 3D content or generate a spatial scene from a 2D image.
  - watchOS: Use SwiftUI to create animations when possible; alternatively use WatchKit to animate a sequence of images.
- **Content/labels:** Supports PNG, JPEG, and PDF image data.
- **APIs:** `Image` (SwiftUI); `UIImageView` (UIKit); `NSImageView` (AppKit); `WKImageAnimatable` (WatchKit); `ImagePresentationComponent` (RealityKit).
- **Web equivalent (translation, not Apple guidance):** `<img>` with meaningful `alt` (or `alt=""` for decorative images), `object-fit` for scale/fit behavior; use `<picture>` for resolution variants; wrap in `<button>` only when the image must be clickable.
- **Source:** [reference](../references/components/content/image-views.md)

### Text views
- **What it is:** A text view displays multiline, styled text content, which can optionally be editable.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You need to display text that's long, editable, or in a special format.
  - Content may need to scroll because it extends beyond the view.
- **Don't use it when / use instead:**
  - You need to display a small amount of text; use a [label](../references/components/layout-and-organization/labels.md).
  - You need a small amount of editable text; use a [text field](../references/components/selection-and-input/text-fields.md).
- **Rules:**
  - Use a text view when you need to display text that's long, editable, or in a special format.
  - Keep text legible; adopt Dynamic Type and test with accessibility options such as bold text turned on.
  - Make useful text selectable (error messages, serial numbers, IP addresses).
  - By default content aligns to the leading edge and uses the system label color.
  - In iOS, iPadOS, and visionOS, a keyboard appears when people select an editable text view.
- **Platform notes:**
  - macOS, visionOS, watchOS: No additional considerations.
  - iOS, iPadOS: Show the appropriate keyboard type for the content being edited (see [Virtual keyboards](../references/components/selection-and-input/virtual-keyboards.md)).
  - tvOS: You can display text in a text view, but tvOS uses text fields for editable text because text input is minimal by design.
- **Content/labels:** Maintain readability even when mixing fonts, colors, and alignments.
- **APIs:** `Text` (SwiftUI); `UITextView` (UIKit); `NSTextView` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<textarea>` (editable) or a block element with `overflow: auto` (read-only); set `inputmode` for the content type; keep `user-select: text` so content stays selectable; respect `font-size` scaling with relative units.
- **Source:** [reference](../references/components/content/text-views.md)

### Web views
- **What it is:** A web view loads and displays rich web content, such as embedded HTML and websites, directly within your app.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - You need to show HTML content inside your app (for example Mail showing HTML messages).
  - People need to briefly access a website without leaving the context of your app.
- **Don't use it when / use instead:**
  - You want to build a web browser; Safari is the primary way people browse the web and replicating it is discouraged.
  - You target tvOS or watchOS; web views aren't supported there.
- **Rules:**
  - Support forward and back navigation when appropriate; it isn't available by default, so provide controls if people will visit multiple pages.
  - Avoid using a web view to build a web browser.
- **Platform notes:**
  - iOS, iPadOS, macOS, visionOS: No additional considerations. Not supported in tvOS or watchOS.
- **Content/labels:** None given.
- **APIs:** `WKWebView` (WebKit).
- **Web equivalent (translation, not Apple guidance):** `<iframe>` with a `title` attribute and a restrictive `sandbox`; add explicit back and forward controls only if the embedded content is navigable.
- **Source:** [reference](../references/components/content/web-views.md)

---

## Layout and organization

### Boxes
- **What it is:** A box creates a visually distinct group of logically related information and components.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - You need to separate a group of related content or controls from the rest of the interface with a border or background color.
  - A title would help people (and VoiceOver users) understand the relationship between the grouped items.
- **Don't use it when / use instead:**
  - The group would be nearly as large as its containing window or screen; the separation stops communicating.
  - You need subgroups inside a box; use padding and alignment rather than nested boxes.
  - You need switchable panes rather than a static group; use [Tab views](../references/components/layout-and-organization/tab-views.md) on macOS.
- **Rules:**
  - Prefer keeping a box relatively small in comparison with its containing view.
  - Consider using padding and alignment to communicate additional grouping within a box; nested boxes make the interface feel busy and constrained.
  - Provide a succinct introductory title if it helps clarify the box's contents.
  - If you need a title, write a brief phrase that describes the contents.
- **Platform notes:**
  - visionOS: No additional considerations. Not supported in tvOS or watchOS.
  - iOS, iPadOS: By default, boxes use the secondary and tertiary background colors.
  - macOS: By default, a box's title appears above it.
- **Content/labels:** Title uses sentence-style capitalization. Avoid ending punctuation unless the box is in a settings pane, where you append a colon to the title.
- **APIs:** `GroupBox` (SwiftUI); `NSBox` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<fieldset>` with `<legend>` for groups of controls, or a `<section>` with an `aria-labelledby` heading and a subtle border or background; keep it small relative to its container.
- **Source:** [reference](../references/components/layout-and-organization/boxes.md)

### Collections
- **What it is:** A collection manages an ordered set of content and presents it in a customizable and highly visual layout.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **Use it when:**
  - You are showing image-based content.
  - Items vary widely in size or you need to display a large number of images.
- **Don't use it when / use instead:**
  - The content is text; it's simpler and more efficient to read in a scrollable [list or table](../references/components/layout-and-organization/lists-and-tables.md).
  - You target watchOS; collections aren't supported.
- **Rules:**
  - Use the standard row or grid layout whenever possible; avoid a custom layout that might confuse people or draw undue attention to itself.
  - Consider using a table instead of a collection for text.
  - Make it easy to choose an item; use adequate padding around images to keep focus or hover effects easy to see and prevent overlap.
  - Add custom interactions when necessary; by default people tap to select, touch and hold to edit, and swipe to scroll.
  - Consider using animations to provide feedback when people insert, delete, or reorder items.
- **Platform notes:**
  - macOS, tvOS, visionOS: No additional considerations. Not supported in watchOS.
  - iOS, iPadOS: Use caution when making dynamic layout changes; avoid changing the layout while people are viewing and interacting unless it's in response to an explicit action.
- **Content/labels:** None given.
- **APIs:** `UICollectionView` (UIKit); `NSCollectionView` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A `<ul role="list">` or `role="grid"` laid out with CSS Grid (`grid-template-columns: repeat(auto-fill, minmax(...))`) or a horizontal flex row with `overflow-x: auto`; give each item a visible focus ring and padding so hover and focus never overlap neighbors.
- **Source:** [reference](../references/components/layout-and-organization/collections.md)

### Column views
- **What it is:** A column view, also called a browser, lets people view and navigate a data hierarchy using a series of vertical columns.
- **Platforms:** macos
- **Use it when:**
  - You have a deep data hierarchy in which people navigate back and forth frequently between levels (for example the Finder's column view).
  - You don't need the sorting capabilities that a list or table provides.
- **Don't use it when / use instead:**
  - You need sortable columns of attributes; use [Lists and tables](../references/components/layout-and-organization/lists-and-tables.md) or an [Outline view](../references/components/layout-and-organization/outline-views.md).
  - You're building for iPadOS or visionOS; consider a [Split view](../references/components/layout-and-organization/split-views.md) for hierarchical content.
- **Rules:**
  - Show the root level of your data hierarchy in the first column so people can scroll back to begin again from the top.
  - Consider showing information about the selected item when there are no nested items to display (preview, creation date, type, size).
  - Let people resize columns, especially if item names are too long for the default width.
  - Mark parent items with a triangle icon; selecting a parent displays its children in the next column.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Content/labels:** None given.
- **APIs:** `NSBrowser` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A Miller-columns layout: a horizontal flex container of `<ul role="listbox">` columns where selecting an option in one column renders its children in the next; make columns resizable and keep the root column always reachable by horizontal scroll.
- **Source:** [reference](../references/components/layout-and-organization/column-views.md)

### Disclosure controls
- **What it is:** Disclosure controls reveal and hide information and functionality related to specific controls or views.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - You want to hide details until they're relevant and keep advanced options out of the way (disclosure triangle for a view or list; disclosure button for a specific control such as the macOS Save sheet).
  - You need to progressively reveal hierarchy in a list (as the Finder does in list view).
- **Don't use it when / use instead:**
  - You'd need more than one disclosure button in a single view; that adds complexity and confusion.
  - You need a full hierarchical table on macOS; use an [Outline view](../references/components/layout-and-organization/outline-views.md).
- **Rules:**
  - Use a disclosure control to hide details until they're relevant; place the most-used controls at the top of the disclosure hierarchy and hide advanced functionality by default.
  - A disclosure triangle points inward from the leading edge when hidden and down when visible.
  - Provide a descriptive label when using a disclosure triangle, like "Advanced Options".
  - A disclosure button points down when content is hidden and up when visible.
  - Place a disclosure button near the content that it shows and hides.
  - Use no more than one disclosure button in a single view.
- **Platform notes:**
  - macOS: No additional considerations. Not supported in tvOS or watchOS.
  - iOS, iPadOS, visionOS: Available through the SwiftUI `DisclosureGroup` view.
- **Content/labels:** Labels indicate what is disclosed or hidden (for example "Advanced Options").
- **APIs:** `DisclosureGroup` (SwiftUI); `NSButton.BezelStyle.disclosure`, `NSButton.BezelStyle.pushDisclosure` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<details>` with `<summary>` (the summary is the triangle plus label), or a `<button aria-expanded aria-controls>` toggling a region; rotate the chevron to match state and keep only one such button per view.
- **Source:** [reference](../references/components/layout-and-organization/disclosure-controls.md)

### Labels
- **What it is:** A label is a static piece of text that people can read and often copy, but not edit.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You need to display a small amount of text that people don't need to edit, for example in buttons, list items, or to introduce a control.
  - You want to communicate relative importance with the system label colors.
- **Don't use it when / use instead:**
  - People need to edit a small amount of text; use a [text field](../references/components/selection-and-input/text-fields.md).
  - You need to display a large amount of text, optionally editable; use a [text view](../references/components/content/text-views.md).
- **Rules:**
  - Use a label to display a small amount of text that people don't need to edit.
  - Prefer system fonts; labels support Dynamic Type by default, and custom fonts must remain legible.
  - Use system-provided label colors to communicate relative importance: Label (primary information), Secondary label (subheading or supplemental text), Tertiary label (unavailable item or behavior), Quaternary label (watermark text).
  - Make useful label text selectable (error messages, locations, IP addresses).
- **Platform notes:**
  - iOS, iPadOS, tvOS, visionOS: No additional considerations.
  - macOS: Use the `isEditable` property of `NSTextField` to display uneditable text.
  - watchOS: Date and time text components display current date or time in configurable formats; countdown timer components display count up or count down values. The system adjusts presentation to fit and updates content automatically; consider them in complications.
- **Content/labels:** In a button, a label conveys what the button does (Edit, Cancel, Send). Component-specific pages (buttons, menus, lists) add more text guidance.
- **APIs:** `Label`, `Text` (SwiftUI); `UILabel`, `UIColor.label`, `secondaryLabel`, `tertiaryLabel`, `quaternaryLabel` (UIKit); `NSTextField`, `NSColor.labelColor`, `secondaryLabelColor`, `tertiaryLabelColor`, `quaternaryLabelColor` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<span>`, `<p>`, or `<label for>` when introducing a control; define four text-color tokens for primary, secondary, tertiary, and quaternary importance; leave text selectable.
- **Source:** [reference](../references/components/layout-and-organization/labels.md)

### Lists and tables
- **What it is:** Lists and tables present data in one or more columns of rows.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You're displaying text, which is easy to scan and read in a row-based format.
  - You want to express an information hierarchy people navigate (like iOS Settings) or show sortable attributes in separate columns.
  - People need to select, add, delete, or reorder items.
- **Don't use it when / use instead:**
  - Items vary widely in size or you need to display a large number of images; use a [Collection](../references/components/layout-and-organization/collections.md).
  - The data is hierarchical on macOS; use an [Outline view](../references/components/layout-and-organization/outline-views.md).
- **Rules:**
  - Prefer displaying text in a list or table.
  - Let people edit a table when it makes sense; people appreciate reordering even if they can't add or remove items. In iOS and iPadOS, people must enter an edit mode before they can select items.
  - Provide appropriate feedback when people select a list item: persistently highlight the selected row in a navigation table, briefly highlight and add a checkmark in a table of options.
  - Keep item text succinct so row content is comfortable to read; if items are long, list titles only and reveal content in a detail view.
  - Consider ways to preserve readability of text that might otherwise get clipped or truncated; a middle ellipsis can keep both the beginning and end.
  - Use descriptive column headings in a multicolumn table; if a single-column table has no heading, use a label or header for context.
  - Choose a table or list style that coordinates with your data and platform (grouped style on iOS and iPadOS, elliptical style on watchOS, bordered style with alternating rows on macOS).
  - Choose a row style that fits the information you need to display (for example a small leading image followed by a label).
- **Platform notes:**
  - iOS, iPadOS, visionOS: Use an info button (detail disclosure button) only to reveal more information about a row's content, never for navigation; use a disclosure indicator accessory to drill into a row. Avoid adding an index to a table that displays trailing controls like disclosure indicators.
  - macOS: When it provides value, let people click a column heading to sort; clicking an already sorted heading reverses the sort. Let people resize columns. Consider alternating row colors in a multicolumn table. Use an outline view instead of a table view for hierarchical data.
  - tvOS: Confirm that images near a table still look good as each focused row highlights, grows slightly, and may round its corners; don't add your own corner masks.
  - watchOS: When possible, limit the number of rows; list the most relevant items and provide a way to view more. Constrain the length of detail views if you want to support vertical page-based navigation, which only works when detail views don't scroll.
- **Content/labels:** Column headings use nouns or short noun phrases with title-style capitalization and no ending punctuation.
- **APIs:** `List`, `Tables`, `ListStyle` (SwiftUI); `UITableView`, `UIListContentConfiguration`, `UITableViewCell.AccessoryType.disclosureIndicator` (UIKit); `NSTableView` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<table>` with `<thead>` and `<th scope="col">` for multicolumn data (sortable headers as `<button>` inside `<th>` with `aria-sort`); `<ul>` or `role="listbox"` for single-column lists; use `text-overflow: ellipsis` and keep selection state visible via `aria-selected`.
- **Source:** [reference](../references/components/layout-and-organization/lists-and-tables.md)

### Lockups
- **What it is:** Lockups combine multiple separate views into a single, interactive unit.
- **Platforms:** tvos
- **Use it when:**
  - You're presenting focusable media items on Apple TV with a header, content view, and footer that expand together on focus.
  - You need one of the four lockup types: cards (ratings and reviews), caption buttons (image or text with title and subtitle), monograms (people), or posters (image with optional title and subtitle revealed on focus).
- **Don't use it when / use instead:**
  - You target any platform other than tvOS; lockups aren't supported.
  - You need a plain non-focusable image; use [Image views](../references/components/content/image-views.md).
- **Rules:**
  - Allow adequate space between lockups; a focused lockup expands, so leave room to avoid overlapping or displacing neighbors.
  - Use consistent lockup sizes within a row or group.
  - Make sure caption buttons tilt with the motion people swipe: up and down when aligned vertically, left and right when horizontal, both in a grid.
  - Prefer images over initials in monograms; an image creates a more intimate connection than text.
  - Size posters appropriately for their content.
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.
- **Content/labels:** Monograms show a circular picture and the person's name, falling back to initials. Posters hide title and subtitle until focused.
- **APIs:** `TVLockupView`, `TVLockupHeaderFooterView`, `TVCardView`, `TVCaptionButtonView`, `TVMonogramContentView`, `TVPosterView` (TVUIKit).
- **Web equivalent (translation, not Apple guidance):** A focusable `<a>` or `<button>` card containing header, media, and footer; on `:focus-visible` scale the whole card together (`transform: scale`) and reserve margin so the enlarged card never overlaps siblings; keep equal sizes within a row.
- **Source:** [reference](../references/components/layout-and-organization/lockups.md)

### Outline views
- **What it is:** An outline view presents hierarchical data in a scrolling list of cells that are organized into columns and rows.
- **Platforms:** macos
- **Use it when:**
  - You're displaying text-based hierarchical content, often in the leading side of a split view (parent containers with disclosure triangles and children).
  - You need extra columns for attributes like size and modification date alongside the hierarchy.
- **Don't use it when / use instead:**
  - The data isn't hierarchical; use [Lists and tables](../references/components/layout-and-organization/lists-and-tables.md).
  - People navigate back and forth frequently between levels of a deep hierarchy and don't need sorting; consider a [Column view](../references/components/layout-and-organization/column-views.md).
- **Rules:**
  - Use a table instead of an outline view to present data that's not hierarchical.
  - Expose data hierarchy in the first column only; other columns display attributes.
  - Use descriptive column headings to provide context; always provide headings in a multi-column outline view.
  - Consider letting people click column headings to sort; sorting the primary column sorts at each hierarchy level, and clicking an already sorted heading reverses the direction.
  - Let people resize columns.
  - Make it easy for people to expand or collapse nested containers (for example Option-click expands all subfolders).
  - Retain people's expansion choices so they don't need to navigate back to the same place again.
  - Consider using alternating row colors in multi-column outline views.
  - Let people edit data if it makes sense; people expect a single click to edit a cell, while a double click can respond differently (for example opening a file).
  - Consider using a centered ellipsis to truncate cell text instead of clipping it.
  - Consider offering a search field in the toolbar to help people find values quickly in a lengthy outline view.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Content/labels:** Column headings are nouns or short noun phrases with title-style capitalization and no punctuation; in particular, avoid a trailing colon.
- **APIs:** `OutlineGroup` (SwiftUI); `NSOutlineView` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<table role="treegrid">` with rows carrying `aria-level`, `aria-expanded`, and `aria-posinset`; a disclosure button in the first column toggles children; persist expansion state (for example in `localStorage`) and support sortable headers.
- **Source:** [reference](../references/components/layout-and-organization/outline-views.md)

### Split views
- **What it is:** A split view manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, collections, images, and custom views.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You want to show multiple levels of your app's hierarchy at once and support navigation between them (selecting in the primary pane shows contents in the secondary pane, optionally a tertiary pane).
  - You're displaying a sidebar for navigation, or rarely, supplementary functionality like Keynote's navigator, presenter notes, and inspector.
- **Don't use it when / use instead:**
  - You're in a compact environment such as iPhone in portrait; prefer a regular environment.
  - In visionOS you need to request a small amount of information or a simple task someone must complete first; use a [sheet](../references/components/presentation/sheets.md).
  - You need a flat set of pages on watchOS; use a vertical [tab view](../references/components/layout-and-organization/tab-views.md) for detail pages.
- **Rules:**
  - To support navigation, persistently highlight the current selection in each pane that leads to the detail view.
  - Consider letting people drag and drop content between panes.
- **Platform notes:**
  - iOS: Prefer using a split view in a regular, not a compact, environment.
  - iPadOS: A split view can include two vertical panes (Mail) or three (Keynote). Account for narrow, compact, and intermediate window widths since iPad windows are fluidly resizable, and ensure people can navigate between panes logically.
  - macOS: Panes can be arranged vertically, horizontally, or both, with draggable dividers. Set reasonable defaults for minimum and maximum pane sizes so the divider stays visible. Consider letting people hide a pane when it makes sense. Provide multiple ways to reveal hidden panes (toolbar button, menu command, keyboard shortcut). Prefer the thin divider style, which measures one point in width; use thicker dividers only with a specific need.
  - tvOS: Works well to filter content. Choose a layout that keeps panes balanced; the default devotes a third of the width to the primary pane and two-thirds to the secondary, or you can specify half-and-half. Display a single title above the split view; don't title each pane. Center the title when the secondary pane holds a collection; place it above the primary view when the secondary pane holds a single main view.
  - visionOS: To display supplementary information, prefer a split view instead of a new window.
  - watchOS: The split view displays either the list view or a detail view full screen. Automatically display the most relevant detail view at launch. If your app displays multiple detail pages, place the detail views in a vertical tab view navigated by the Digital Crown with a page indicator.
- **Content/labels:** On tvOS, one title for the whole split view.
- **APIs:** `NavigationSplitView`, `VSplitView`, `HSplitView` (SwiftUI); `UISplitViewController` (UIKit); `NSSplitViewController`, `NSSplitView.DividerStyle` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A CSS Grid or flex layout of `<nav>`/`<aside>` and `<main>` panes with a 1px `role="separator"` divider (`aria-orientation`, `aria-valuenow`) that is keyboard-resizable; collapse to a single stacked pane below a compact breakpoint and keep the selected row highlighted with `aria-current`.
- **Source:** [reference](../references/components/layout-and-organization/split-views.md)

### Tab views
- **What it is:** A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.
- **Platforms:** macos, watchos
- **Use it when:**
  - You're presenting closely related areas of content where each pane is similar or related to the others (macOS).
  - You need page-by-page content on watchOS, where tab views display as pages with a page control.
- **Don't use it when / use instead:**
  - You need more than six tabs; present each pane as a view option in a pop-up button menu instead.
  - You're switching between separate sections of an app; use a [Tab bar](../references/components/navigation-and-search/tab-bars.md).
  - You're on iOS or iPadOS; use a [Segmented control](../references/components/selection-and-input/segmented-controls.md) for similar functionality.
- **Rules:**
  - Use a tab view to present closely related areas of content.
  - Make sure the controls within a pane affect content only in the same pane; panes are self-contained.
  - Provide a label for each tab that describes the contents of its pane.
  - Avoid using a pop-up button to switch between tabs; a tabbed control needs one click and shows all choices at once (a pop-up button is reasonable only when there are too many panes for tabs).
  - Avoid providing more than six tabs in a tab view.
  - In general, inset a tab view by leaving a margin of window-body area on all sides; extending to the window edges is unusual.
  - You can hide the tabbed control when an app switches panes programmatically; the content area can then be borderless, bezeled, or bordered with a line.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, or visionOS.
  - iOS, iPadOS: Consider a segmented control instead.
  - watchOS: Tab views display using page controls; the page indicator next to the Digital Crown shows the current page and that people can scroll within the page.
- **Content/labels:** Use nouns or short noun phrases for tab labels (a verb may make sense in some contexts) with title-style capitalization.
- **APIs:** `TabView` (SwiftUI); `NSTabView` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `role="tablist"` with `<button role="tab" aria-selected aria-controls>` and `role="tabpanel"` regions; arrow keys move between tabs; cap at six tabs and fall back to a `<select>` beyond that.
- **Source:** [reference](../references/components/layout-and-organization/tab-views.md)

---

## Menus and actions

### Activity views
- **What it is:** An activity view, often called a share sheet, presents a range of tasks that people can perform in the current context.
- **Platforms:** ios, ipados, visionos
- **Use it when:**
  - People choose the Share button while viewing a page or document, or after selecting an item, and you want to offer system sharing activities, actions like Copy and Print, and frequently used apps.
  - You want to offer app-specific activities (like Photos' Copy Photo or Add to Album) alongside system ones.
  - You want to provide share or action extensions that people can use in other apps.
- **Don't use it when / use instead:**
  - You need an alternative way to do the same thing as the Share button; use the Share button, not a custom entry point.
  - You need a long-running operation to finish inside the view; the activity view dismisses immediately, so continue in your main app.
  - You're on macOS; there is no activity view, but share and action extensions still work.
- **Rules:**
  - Avoid creating duplicate versions of common actions that are already available in the activity view; if you need something similar, give it a custom title like "Print Transaction".
  - Consider using a symbol to represent your custom activity; if you create a custom interface icon, center it in an area measuring about 70x70 pixels.
  - Write a succinct, descriptive title for each custom action you provide; long titles wrap and may truncate.
  - Make sure activities are appropriate for the current context; exclude system tasks that don't apply (for example Print) and decide which custom tasks to show.
  - Use the Share button to display an activity view.
  - If necessary, create a custom extension interface that feels familiar; prefer the system composition view for share extensions, and include your app name in an action extension.
  - Streamline and limit interaction so people finish in a few steps.
  - Avoid placing a modal view above your extension; an alert may be necessary, additional modal views aren't.
  - If necessary, provide an image that communicates the purpose of your extension; share extensions use the app icon automatically, action extensions should use a symbol or interface icon.
  - Use your main app to denote the progress of a lengthy operation; don't notify people simply because the task completes.
- **Platform notes:**
  - iOS, iPadOS, visionOS: No additional considerations. Not supported in macOS, tvOS, or watchOS.
  - Presentation: an activity view can appear as a sheet or a popover depending on device and orientation. In macOS, share extensions are reached from a Share toolbar button or a context menu; action extensions from hovering embedded content, a toolbar button, or Finder quick actions.
- **Content/labels:** Action titles: a single verb or brief verb phrase; avoid your company or product name. Share activity titles (typically a company name) appear below the icon.
- **APIs:** `UIActivityViewController`, `UIActivity` (UIKit); App Extension Support (Foundation).
- **Web equivalent (translation, not Apple guidance):** Call `navigator.share()` from a Share `<button>` when available; otherwise open a `<dialog>` listing share targets and actions as buttons with verb labels; never duplicate what the native share sheet already offers.
- **Source:** [reference](../references/components/menus-and-actions/activity-views.md)

### Buttons
- **What it is:** A button initiates an instantaneous action.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - People need a simple, familiar way to perform a task now.
  - You need to communicate a hierarchy of actions through style (prominent for the most likely action), content (symbol, text, or both), and role (normal, primary, cancel, destructive).
- **Don't use it when / use instead:**
  - You need a pair of opposing states; use [Toggles](../references/components/selection-and-input/toggles.md).
  - You need to choose from mutually exclusive options; use [Pop-up buttons](../references/components/menus-and-actions/pop-up-buttons.md) or [Segmented controls](../references/components/selection-and-input/segmented-controls.md).
  - You need a menu of related commands; use [Pull-down buttons](../references/components/menus-and-actions/pull-down-buttons.md).
- **Rules:**
  - Make buttons easy for people to use; a button needs a hit region of at least 44x44 pt, and in visionOS 60x60 pt.
  - Always include a press state for a custom button.
  - In general, use a button that has a prominent visual style for the most likely action in a view; keep prominent buttons to one or two per view.
  - Use style, not size, to visually distinguish the preferred choice among multiple options; same-size buttons signal a coherent set.
  - Avoid applying a similar color to button labels and content layer backgrounds; prefer the default monochromatic label appearance over colorful content.
  - Ensure that each button clearly communicates its purpose with a symbol, a text label, or both.
  - Try to associate familiar actions with familiar icons (for example `square.and.arrow.up` for Share).
  - Consider using text when a short label communicates more clearly than an icon.
  - Assign the primary role to the button people are most likely to choose; it responds to Return and can close a sheet, editable view, or alert.
  - Don't assign the primary role to a button that performs a destructive action, even if that action is the most likely choice.
  - A primary button uses the app's accent color; a destructive button uses the system red color.
- **Platform notes:**
  - tvOS: No additional considerations.
  - iOS, iPadOS: Configure a button to display an activity indicator when an action doesn't instantly complete, optionally with a different label (for example "Checkout" becomes "Checking out…"); the system hides the button image while the indicator shows.
  - macOS: Push buttons are the standard type; use a flexible-height push button only for tall or variable height content (two lines of text or a tall icon). Append a trailing ellipsis to the title when a push button opens another window, view, or app. Consider supporting spring loading. Square (gradient) buttons contain symbols or icons, not text, sit within or beneath their view, and belong in a view, not the window frame; prefer a symbol; avoid labels introducing them. Help buttons: use the system-provided help button, open the help topic related to the current context, include no more than one per window, position per the table (dialog with dismissal buttons: lower corner opposite the dismissal buttons and vertically aligned with them; dialog without dismissal buttons or settings window: lower-left or lower-right corner), use within a view not the window frame, and avoid introductory text. Image buttons: use in a view not the window frame, include about 10 pixels of padding between image edges and button edges, avoid a system border, and position any label below the button.
  - visionOS: Buttons usually have a visible background and play sound on interaction. Icon-only buttons use the circle shape, text-only use roundedRectangle or capsule, icon-plus-text use capsule. Sizes: Mini 28 pt, Small 32 pt, Regular 44 pt, Large 52 pt, Extra large 64 pt (circular supports all five; capsule text-only and rounded rectangle support Small through Large; capsule text-and-icon supports Regular and Large). Four states: idle, hover, selected, unavailable; custom hover effects aren't supported. Prefer buttons with a discernible background shape and fill (thin material on a glass window, glass material floating in space), except in toolbars, context menus, alerts, and ornaments. Avoid a custom button with a white fill and black text or icons, which the system reserves for the toggled state. Prefer circular or capsule-shape buttons; prefer a capsule for a lone button. Place button centers at least 60 pt apart; add 4 pt of padding around buttons 60 pt or larger; avoid stacking small or mini buttons. Prefer rounded-rectangle shapes in a vertical stack and capsules in a horizontal row. Use standard controls for familiar audible feedback since visionOS doesn't play haptics.
  - watchOS: All inline buttons use the capsule shape with a material effect. Use a toolbar to place buttons in the corners (the system moves time and title and applies Liquid Glass). Prefer buttons that span the width of the screen for primary actions; if two share a row, use the same height and images or short titles. Use toolbar buttons for navigation to related areas or contextual actions. Use the same height for vertical stacks of one- and two-line text buttons.
- **Content/labels:** Text labels use title-style capitalization and often start with a verb ("Add to Cart"). macOS and visionOS show a tooltip on hover; text buttons in visionOS generally don't need one.
- **APIs:** `Button`, `ButtonBorderShape.circle`, `.roundedRectangle`, `.capsule`, `Material.thin` (SwiftUI); `UIButton` (UIKit); `NSButton`, `NSButton.BezelStyle.flexiblePush`, `NSButton.BezelStyle.smallSquare`, `isBordered` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<button type="button">` (or `type="submit"` for the primary/default action so Enter triggers it); minimum 44x44 CSS px target with `:active` and `:focus-visible` styles; expose destructive styling via a class, never make a destructive button the default; use `aria-busy` plus an inline spinner for pending actions.
- **Source:** [reference](../references/components/menus-and-actions/buttons.md)

### Context menus
- **What it is:** A context menu provides access to functionality that's directly related to an item, without cluttering the interface.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **Use it when:**
  - People need quick access to the commands they're most likely to need for a selected view or content (touch and hold, pinch and hold, Control-click, or secondary click).
  - In visionOS, you want frequently used functionality without opening a panel or inspector window.
- **Don't use it when / use instead:**
  - You want to expose advanced or rarely used items; those belong in the main interface or menu bar.
  - The item already offers an [Edit menu](../references/components/menus-and-actions/edit-menus.md) on iOS or iPadOS; provide one or the other, not both.
  - You target watchOS; context menus aren't supported.
- **Rules:**
  - Prioritize relevancy when choosing items to include in a context menu.
  - Aim for a small number of menu items.
  - Support context menus consistently throughout your app.
  - Always make context menu items available in the main interface, too.
  - If you need to use submenus to manage a menu's complexity, keep them to one level and give each an intuitive title.
  - Hide unavailable menu items, don't dim them (macOS exceptions: Cut, Copy, and Paste may appear unavailable).
  - Aim to place the most frequently used menu items where people are likely to encounter them first; reverse the order if the menu opens above the content.
  - Show keyboard shortcuts in your app's main menus, not in context menus.
  - Follow best practices for using separators; in general, no more than about three groups.
  - In iOS, iPadOS, and visionOS, warn people about context menu items that can destroy data; list them at the end and mark them destructive (red text).
  - Include a title in a context menu only if doing so clarifies the menu's effect (for example the number of selected messages).
  - Represent menu item actions with familiar icons, using the same icons as the system for Copy, Share, Delete, and so on.
- **Platform notes:**
  - tvOS: No additional considerations. Not supported in watchOS.
  - iOS, iPadOS: Provide either a context menu or an edit menu for an item, but not both. In iPadOS, consider using a context menu to let people create a new object (as Files does for new folders). A context menu can show a preview of the content; prefer a graphical preview that clarifies the target of the commands, and ensure the preview looks good as it animates by matching its clipping path to the image shape.
  - macOS: Sometimes called a contextual menu.
  - visionOS: Consider a context menu instead of a panel or inspector window for frequently used functionality. In general, avoid letting a context menu's height exceed the height of the window, because it could obscure system components above and below the window.
- **Content/labels:** Context menus seldom display a title; each item needs a short label that clearly describes what it does (see Menus > Labels).
- **APIs:** `contextMenu(menuItems:)` (SwiftUI); `UIContextMenuInteraction`, `UIContextMenuInteractionDelegate`, `UIMenuElement.Attributes.destructive` (UIKit); `NSMenu.popUpContextMenu(_:with:for:)` (AppKit).
- **Web equivalent (translation, not Apple guidance):** Listen for `contextmenu` and long-press, then show a `role="menu"` of `role="menuitem"` buttons positioned at the pointer; omit unavailable items instead of disabling them, put destructive items last with a danger style, close on Escape and outside click, and keep every command available elsewhere in the UI.
- **Source:** [reference](../references/components/menus-and-actions/context-menus.md)

### Dock menus
- **What it is:** On a Mac, people can secondary click an app's or game's icon in the Dock to reveal a Dock menu, which presents both system-provided and custom items.
- **Platforms:** macos
- **Use it when:**
  - You want to list currently or recently open windows so people can jump to one.
  - You want to offer a few actions that are useful when your app isn't frontmost or has no open windows (Mail offers Get New Mail and New Message).
- **Don't use it when / use instead:**
  - The command exists only in the Dock menu; always offer it in the menu bar or interface too.
  - You're on iOS or iPadOS; use [Home Screen quick actions](../references/components/menus-and-actions/home-screen-quick-actions.md).
- **Rules:**
  - Label Dock menu items succinctly and organize them logically, as with all menus.
  - Make custom Dock menu items available in other places, too.
  - Prefer high-value custom items for your Dock menu.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Content/labels:** Follow [Menus](../references/components/menus-and-actions/menus.md) labeling guidance.
- **APIs:** `applicationDockMenu(_:)` (AppKit, `NSApplicationDelegate`).
- **Web equivalent (translation, not Apple guidance):** No direct equivalent; the closest is an installed PWA's app shortcuts in the manifest (`shortcuts` array), which should list a few high-value entry points also reachable inside the app.
- **Source:** [reference](../references/components/menus-and-actions/dock-menus.md)

### Edit menus
- **What it is:** An edit menu lets people make changes to selected content in the current view, in addition to offering related commands like Copy, Select, Translate, and Look Up.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - People select text or other selectable content (images, files, contact cards, charts, map locations) and need editing or related commands.
  - The system can detect a data type (an address adds Get directions, for example).
- **Don't use it when / use instead:**
  - You'd be creating a custom menu that presents the same commands as the system-provided one; prefer the system edit menu.
  - The same item already has a [Context menu](../references/components/menus-and-actions/context-menus.md) on iOS or iPadOS; provide one or the other.
  - You target tvOS or watchOS, where editing is rare and no edit menu exists.
- **Rules:**
  - Prefer the system-provided edit menu.
  - Let people reveal an edit menu using the system-defined interactions they already know (touch and hold, pinch and hold, secondary click).
  - Offer commands that are relevant in the current context, removing or dimming commands that don't apply (no Copy with nothing selected, no Paste with nothing to paste).
  - List custom commands near relevant system-provided ones, and avoid overwhelming people with too many custom commands.
  - When it makes sense, let people select and copy noneditable text; in general let people copy content text, but not control labels.
  - Support undo and redo when possible, because menu actions don't require confirmation.
  - In general, avoid implementing other controls that perform the same functions as edit menu items.
  - Differentiate different types of deletion commands when necessary (Delete behaves like the Delete key; Cut copies to the pasteboard first).
- **Platform notes:**
  - visionOS: No additional considerations. Not supported in tvOS or watchOS.
  - iOS, iPadOS: Ensure your edit menu works well in both styles: the compact horizontal style for Multi-Touch and the vertical style for keyboard or pointing device. Adjust an edit menu's placement if necessary to avoid covering important content; you can't change its shape or pointer.
  - macOS: Editing commands appear in a context menu and in the Edit menu in the menu bar; see the menu bar page for item order.
  - iOS: people tap a chevron on the trailing edge to expand the compact menu into a context menu.
- **Content/labels:** Create short labels for custom commands using verbs or short verb phrases.
- **APIs:** `UIEditMenuInteraction`, `UIResponderStandardEditActions` (UIKit); `NSMenu` (AppKit).
- **Web equivalent (translation, not Apple guidance):** Rely on the browser's native selection menu for Copy, Cut, and Paste; if you add custom selection actions, show a small floating `role="toolbar"` anchored to the selection with verb-labeled buttons, and support `Ctrl/Cmd+Z` undo.
- **Source:** [reference](../references/components/menus-and-actions/edit-menus.md)

### Home Screen quick actions
- **What it is:** Home Screen quick actions give people a way to perform app-specific actions from the Home Screen.
- **Platforms:** ios, ipados
- **Use it when:**
  - You can offer compelling, high-value tasks people can start without opening the app (Maps: search nearby, directions home).
  - You want dynamic actions that update with new information (Messages: recent conversations).
- **Don't use it when / use instead:**
  - You need more than four actions; you can provide a total of four.
  - You're on macOS; use [Dock menus](../references/components/menus-and-actions/dock-menus.md).
- **Rules:**
  - Create quick actions for compelling, high-value tasks; people expect at least one useful quick action and you can provide a total of four.
  - Avoid making unpredictable changes to quick actions; dynamic changes should be ones people can predict.
  - For each quick action, provide a succinct title that instantly communicates the results of the action; add a subtitle if more context helps.
  - Provide a familiar interface icon for each quick action, preferring SF Symbols; for custom icons use the Quick Action Icon Template from Apple Design Resources.
  - Don't use an emoji in place of a symbol or interface icon; quick action symbols are monochromatic and adapt to Dark Mode.
- **Platform notes:**
  - iOS, iPadOS: No additional considerations. Not supported in macOS, tvOS, visionOS, or watchOS.
  - Anatomy: each action has a title, an interface icon on the left or right depending on the app icon's position, and an optional subtitle; title and subtitle are always left-aligned in left-to-right languages.
- **Content/labels:** Titles like "Directions Home", "Create New Contact", "New Message". Don't include your app name or extraneous information; keep text short to avoid truncation and account for localization.
- **APIs:** Add Home Screen quick actions (UIKit).
- **Web equivalent (translation, not Apple guidance):** Web app manifest `shortcuts` (up to a handful of entries, each with a short verb-led `name`, optional `description`, monochrome-friendly icon, and deep-link `url`).
- **Source:** [reference](../references/components/menus-and-actions/home-screen-quick-actions.md)

### Menus
- **What it is:** A menu reveals its options when people interact with it, making it a space-efficient way to present commands in your app or game.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You need to present commands, options, or states that affect the current selection or context without taking permanent screen space.
  - You're labeling and organizing items for any menu type (pop-up, pull-down, context, menu bar, in-game).
- **Don't use it when / use instead:**
  - You need a flat list of mutually exclusive options tied to a control; use a [Pop-up button](../references/components/menus-and-actions/pop-up-buttons.md).
  - You need a few frequently used, item-specific actions; use a [Context menu](../references/components/menus-and-actions/context-menus.md).
  - You need to show all of an app's commands on Mac or iPad; use [The menu bar](../references/components/menus-and-actions/the-menu-bar.md).
- **Rules:**
  - For each menu item, write a label that clearly and succinctly describes it; use a verb or verb phrase for actions (View, Close, Select).
  - To be consistent with platform experiences, use title-style capitalization.
  - Remove articles like a, an, and the from menu-item labels to save space.
  - Show people when a menu item is unavailable (dimmed, unresponsive); if all items are unavailable, keep the menu itself available.
  - Append an ellipsis to a menu item's label when the action requires more information before it can complete.
  - Represent common actions consistently with the standard system icons (Share, Print, Search).
  - Use menu item icons sparingly and with purpose; don't display an icon if you can't find one that clearly represents the item.
  - Apply a uniform visual treatment across menu items in the same group: icons for all items in a group, or none.
  - Prefer listing important or frequently used menu items first.
  - Consider grouping logically related items with separators.
  - Prefer keeping all logically related commands in the same group, even if they differ in importance (Paste and Paste and Match Style).
  - Be mindful of menu length; divide into separate menus or use a submenu, except for user-defined or dynamic content like History and Bookmarks where scrolling is acceptable.
  - Use submenus sparingly; consider one when a term appears in more than two items of a group (Sort by Date, Score, Time becomes Sort by with a submenu).
  - Limit the depth and length of submenus; restrict to a single level, and if a submenu holds more than about five items consider a new menu.
  - Make sure a submenu remains available even when its nested menu items are unavailable.
  - Prefer using a submenu to indenting menu items.
  - Consider using a changeable label that describes an item's current state (Show Map / Hide Map).
  - Include a verb if a changeable label isn't clear enough (Turn HDR On / Turn HDR Off).
  - If necessary, display both menu items instead of one toggled item.
  - Consider using a checkmark to show that an attribute is currently in effect.
  - Consider offering a menu item that makes it easy to remove multiple toggled attributes (for example Plain).
  - In-game menus: let players navigate using the platform's default interaction method, and make sure menus remain easy to open and read on all platforms you support.
- **Platform notes:**
  - macOS, tvOS, watchOS: No additional considerations.
  - iOS, iPadOS: Three layouts. Small: a row of four symbol-only items above the list. Medium: a row of three items with symbol above a short label. Large (default): all items in a list. Choose a small or medium layout when it can help streamline people's choices; use medium for three important frequent actions (Notes: Scan, Lock, Pin) and small only for closely related actions that appear as a group (Bold, Italic, Underline, Strikethrough).
  - visionOS: Supports the small and large layouts. Menus can be presented from 3D content and can appear outside the window's boundaries. Prefer displaying a menu near the content it controls. Prefer the subtle breakthrough effect in most cases (automatic applies subtle when overlapping 3D content); use prominent only when the menu must be visible over the whole scene, and none to fully occlude.
- **Content/labels:** Title-style capitalization; verbs for actions; no articles; ellipsis when more input is needed; a game may follow its own writing style.
- **APIs:** `Menu`, `presentationBreakthroughEffect(_:)`, `BreakthroughEffect.automatic`, `.subtle`, `.prominent`, `.none` (SwiftUI); `UIMenu.preferredElementSize`, Menus and shortcuts (UIKit); Menus (AppKit).
- **Web equivalent (translation, not Apple guidance):** `role="menu"` with `role="menuitem"`, `menuitemcheckbox`, or `menuitemradio` children, `role="separator"` between groups, `aria-haspopup` on submenu items (one level only), `aria-disabled` for unavailable items, arrow-key navigation, Escape to close; title-case labels.
- **Source:** [reference](../references/components/menus-and-actions/menus.md)

### Ornaments
- **What it is:** In visionOS, an ornament presents controls and information related to a window, without crowding or obscuring the window's contents.
- **Platforms:** visionos
- **Use it when:**
  - You need frequently needed controls or information in a consistent location that doesn't clutter the window (Music's Now Playing controls).
  - You're building a custom component that should float on a window's edge, parallel to and slightly in front of it.
- **Don't use it when / use instead:**
  - You need a toolbar or tab bar; use the system-provided [Toolbars](../references/components/menus-and-actions/toolbars.md) and [Tab bars](../references/components/navigation-and-search/tab-bars.md), which automatically appear as ornaments.
  - The window already carries several ornaments; consider relocating elements into the main window.
- **Rules:**
  - Consider using an ornament to present frequently needed controls or information in a consistent location that doesn't clutter the window.
  - In general, keep an ornament visible; hiding it can make sense when people dive into a video or photo.
  - If you need to display multiple ornaments, prioritize the overall visual balance of the window and consider constraining the total number.
  - Aim to keep an ornament's width the same or narrower than the width of the associated window so it doesn't interfere with a vertical tab bar.
  - Consider using borderless buttons in an ornament; the glass background makes borders unnecessary and the system applies the hover effect.
  - Use system-provided toolbars and tab bars unless you need to create custom components.
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.
  - Behavior: an ornament moves with its window; if the window's contents scroll, the ornament's content stays unchanged.
- **Content/labels:** None given.
- **APIs:** `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)` (SwiftUI).
- **Web equivalent (translation, not Apple guidance):** A `position: sticky` or `fixed` `role="toolbar"` pinned to a container edge with a translucent backdrop (`backdrop-filter`), no wider than the container, holding borderless icon buttons; keep it visible except in immersive media views.
- **Source:** [reference](../references/components/menus-and-actions/ornaments.md)

### Pop-up buttons
- **What it is:** A pop-up button displays a menu of mutually exclusive options.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - You need a flat list of mutually exclusive options or states that affect content or the surrounding view (for example Calendar's Repeat setting).
  - Space is limited and you don't need to display all options all the time.
- **Don't use it when / use instead:**
  - You need to offer a list of actions, let people select multiple items, or include a submenu; use a [Pull-down button](../references/components/menus-and-actions/pull-down-buttons.md).
  - People should see all choices at once in a small set; consider a [Segmented control](../references/components/selection-and-input/segmented-controls.md).
  - You're switching tabs in a macOS tab view; use the tabbed control, unless there are too many panes.
- **Rules:**
  - Use a pop-up button to present a flat list of mutually exclusive options or states.
  - Provide a useful default selection; it shows until people choose, so make it the item most people are likely to want.
  - Give people a way to predict a pop-up button's options without opening it (an introductory label or a descriptive button label).
  - Consider using a pop-up button when space is limited and you don't need to display all options all the time.
  - If necessary, include a Custom option in a pop-up button's menu to provide additional items useful in some situations; you can display explanatory text below the list.
  - After people choose an item, the menu closes and the button can update its content to indicate the current selection.
- **Platform notes:**
  - iOS, macOS, visionOS: No additional considerations. Not supported in tvOS or watchOS.
  - iPadOS: Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item when the set of options is small and well-defined.
- **Content/labels:** Label the button with its effect or precede it with an introductory label so the options are predictable.
- **APIs:** `MenuPickerStyle` (SwiftUI); `UIButton.changesSelectionAsPrimaryAction` (UIKit); `NSPopUpButton` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<select>` with a sensible default `<option selected>` and an associated `<label>`; for a custom look, a `<button aria-haspopup="listbox" aria-expanded>` opening a `role="listbox"` whose chosen option becomes the button's text.
- **Source:** [reference](../references/components/menus-and-actions/pop-up-buttons.md)

### Pull-down buttons
- **What it is:** A pull-down button displays a menu of items or actions that directly relate to the button's purpose.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - You need to present commands or items directly related to the button's action (Add presents what to add; Sort presents attributes; Back presents locations to revisit).
  - You have at least three items to list, so the interaction feels worthwhile.
- **Don't use it when / use instead:**
  - You need a list of mutually exclusive choices that aren't commands; use a [Pop-up button](../references/components/menus-and-actions/pop-up-buttons.md).
  - You'd list only one or two items; use buttons for actions and toggles or switches for selections.
  - You'd hide all of a view's primary actions in it; primary actions need to stay discoverable.
- **Rules:**
  - Use a pull-down button to present commands or items that are directly related to the button's action.
  - Avoid putting all of a view's actions in one pull-down button.
  - Balance menu length with ease of use; a minimum of three items makes the interaction worthwhile, too many slows people down.
  - Display a succinct menu title only if it adds meaning.
  - Let people know when a pull-down button's menu item is destructive (red text), and ask them to confirm their intent via an [action sheet](../references/components/presentation/action-sheets.md) (iOS) or [popover](../references/components/presentation/popovers.md) (iPadOS).
  - Include an interface icon with a menu item when it provides value, displayed after its label; SF Symbols stay aligned with text at every scale.
  - After people choose an item, the menu closes and the app performs the chosen action.
- **Platform notes:**
  - macOS, visionOS: No additional considerations. Not supported in tvOS or watchOS.
  - iOS, iPadOS: You can also reveal a pull-down menu with a gesture on a button (Safari's touch and hold on the Tabs button). Consider using a More pull-down button (ellipsis icon) for items that don't need prominent positions, weighing its size convenience against discoverability.
- **Content/labels:** Menu title only when it adds meaning; destructive items in red.
- **APIs:** `MenuPickerStyle` (SwiftUI); `UIControl.showsMenuAsPrimaryAction` (UIKit); `NSPopUpButton.pullsDown` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<button aria-haspopup="menu" aria-expanded>` opening a `role="menu"` of action `menuitem`s (three or more); mark destructive items with a danger style and confirm them in a dialog; don't move every primary action into a single "More" menu.
- **Source:** [reference](../references/components/menus-and-actions/pull-down-buttons.md)

### The menu bar
- **What it is:** On a Mac or an iPad, the menu bar at the top of the screen displays the top-level menus in your app or game.
- **Platforms:** ipados, macos
- **Use it when:**
  - You're building a macOS or iPadOS app and need to list all the commands people can perform, with keyboard shortcuts, in the familiar order.
  - You want people to learn what your app does and find commands even when they're unavailable.
- **Don't use it when / use instead:**
  - You want the menu bar to be the only place for a function on iPad; it's often hidden full screen, so provide access through the UI too.
  - You need item-specific, frequently used commands; those also belong in [Context menus](../references/components/menus-and-actions/context-menus.md) and [Toolbars](../references/components/menus-and-actions/toolbars.md) (but every toolbar item must still be a menu bar command on macOS).
- **Rules:**
  - Menu order: YourAppName, File, Edit, Format, View, app-specific menus, Window, Help (macOS also has the Apple menu leading and menu bar extras trailing).
  - Support the default system-defined menus and their ordering; the system implements much standard functionality for you.
  - Always show the same set of menu items; disable unavailable actions instead of hiding them.
  - Represent menu item actions with familiar icons, the same ones the system uses for Copy, Share, Delete.
  - Support the keyboard shortcuts defined for the standard menu items you include; define custom shortcuts only when necessary.
  - Prefer short, one-word menu titles; use title-style capitalization if more than one word.
  - App menu: Display the About menu item first, followed by a separator. Items in order: About YourAppName (short name of 16 characters or fewer, no version number), Settings… (app-level settings only; document-specific settings go in File), optional app-specific items (after Settings, same group), Services (macOS only), Hide YourAppName, Hide Others, Show All (macOS only), Quit YourAppName (Option changes it to Quit and Keep Windows).
  - File menu (rename or eliminate if your app doesn't handle files): New Item, Open (ellipsis if a separate selection interface), Open Recent (recognizable names, no file paths, most recent first, Clear Menu), Close (Option: Close All; Close Tab in tab-based windows, consider Close Window), Close Tab, Close File, Save (autosave periodically; prompt for name and location on new documents; prefer a pop-up for formats in the Save sheet), Save All, Duplicate (Option: Save As; prefer Duplicate over Save As, Export, Copy To, Save To), Rename…, Move To…, Export As… (reserve for formats your app doesn't typically handle), Revert To, Page Setup… (document-specific printing parameters; global or frequent ones belong in Print), Print….
  - Edit menu: Determine whether Find menu items belong in the Edit menu or the File menu. Order: Undo and Redo (clarify the target, like Undo Paste and Match Style or Undo Typing), Cut, Copy, Paste, Paste and Match Style, Delete (provide Delete instead of Erase or Clear), Select All, Find submenu, Spelling and Grammar, Substitutions, Transformations, Speech, Start Dictation and Emoji & Symbols (added automatically).
  - Format menu (exclude if no formatted text editing): Font submenu, Text submenu.
  - View menu: Provide a View menu even if your app supports only a subset of the standard view functions. Ensure that each show/hide item title reflects the current state (Show Toolbar when hidden, Hide Toolbar when visible). Items: Show/Hide Tab Bar, Show All Tabs/Exit Tab Overview, Show/Hide Toolbar, Customize Toolbar, Show/Hide Sidebar, Enter/Exit Full Screen. The View menu never manages specific windows.
  - App-specific menus: Provide app-specific menus for custom commands, even those available elsewhere. As much as possible, reflect your app's hierarchy (Mail: Mailbox, Message, Format). Aim to list app-specific menus in order from most to least general or commonly used.
  - Window menu: Provide a Window menu even if your app has only one window, with Minimize and Zoom for Full Keyboard Access. Consider including menu items for showing and hiding panels (not the font or color panels, which Format covers). Items: Minimize (Option: Minimize All), Zoom (Option: Zoom All; don't use Zoom for full screen), Show Previous Tab, Show Next Tab, Move Tab to New Window, Merge All Windows, Enter/Exit Full Screen (only if there is no View menu), Bring All to Front (Option: Arrange in Front), open windows in alphabetical order (no panels or modal views).
  - Help menu: Send YourAppName Feedback to Apple, YourAppName Help, additional items after a separator; keep the total small.
  - Dynamic menu items: Avoid making a dynamic menu item the only way to accomplish a task. Use dynamic menu items primarily in menu bar menus. Require only a single modifier key to reveal a dynamic menu item.
- **Platform notes:**
  - Not supported in iOS, tvOS, visionOS, or watchOS.
  - iPadOS: Revealed by moving the pointer to the top edge or swiping down; it occupies the status bar's vertical space. Differences from macOS: hidden until revealed (macOS visible by default); centered (macOS leading); no menu bar extras; window controls in the menu bar when full screen; no Apple menu; About, Services, and visibility items unavailable in the App menu. Because the menu bar is often hidden full screen, ensure that people can access all of your app's functions through its UI, and don't use the menu bar as a catch-all. Reserve the YourAppName > Settings menu item for opening your app's page in iPadOS Settings; link an internal preferences area with a separate item beneath it. For apps with tab-style navigation, consider adding each tab as a menu item in the View menu with key bindings. Consider grouping menu items into submenus to conserve vertical space, since iPad rows are taller.
  - macOS: The Apple menu is always first and can't be modified. The system may compress or truncate menu titles when space is constrained, and the menu bar hides in full-screen mode until the pointer reaches the top. Menu bar extras: consider using a symbol (black and clear colors; the menu bar's height is 24 pt); display a menu, not a popover, when people click your menu bar extra; let people, not your app, decide whether to put your extra in the menu bar (offer it during setup); avoid relying on the presence of menu bar extras; consider exposing the functionality in other ways too, such as a Dock menu.
- **Content/labels:** One-word titles; title-style capitalization; app name in bold identifies the active app; ellipsis for items requiring more input; Undo/Redo append the operation name.
- **APIs:** `CommandMenu`, `MenuBarExtra` (SwiftUI); Adding menus and shortcuts to the menu bar and user interface (UIKit); `NSStatusBar`, `NSMenuItem.isAlternate`, `NSHelpManager` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A top-level `role="menubar"` of `role="menuitem"` buttons each opening a `role="menu"`, in the order App, File, Edit, Format, View, custom, Window, Help; show every item always and use `aria-disabled` rather than hiding; display keyboard shortcuts as `<kbd>` and bind them globally.
- **Source:** [reference](../references/components/menus-and-actions/the-menu-bar.md)

### Toolbars
- **What it is:** A toolbar provides convenient access to frequently used commands, controls, navigation, and search.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You need to present the current view's title, navigation controls (back, forward, search), and actions that act on the view's content, arranged horizontally along the top or bottom edge.
  - You need controls that act on elements in the current view.
- **Don't use it when / use instead:**
  - You need to navigate between areas of an app; use a [Tab bar](../references/components/navigation-and-search/tab-bars.md).
  - You'd add an overflow menu yourself; the system adds one automatically in macOS and iPadOS.
  - On macOS, a square, help, or image button belongs in the window body, not the toolbar; use a toolbar item instead.
- **Rules:**
  - Choose items deliberately to avoid overcrowding; define which items move to the overflow menu as the toolbar narrows, and avoid layouts that overflow by default.
  - Add a More menu to contain additional actions; prioritize less important actions for it and only add it if you really need it.
  - In iPadOS and macOS apps, consider letting people customize the toolbar to include their most common items.
  - Reduce the use of toolbar backgrounds and tinted controls; let the content layer inform the toolbar's appearance and use a scroll edge effect when necessary.
  - Avoid applying a similar color to toolbar item labels and content layer backgrounds; prefer the default monochromatic appearance over colorful content.
  - Prefer using standard components in a toolbar; custom components need corner radii concentric with the bar's corners.
  - Consider temporarily hiding toolbars for a distraction-free experience, and offer ways to reliably restore them.
  - Provide a useful title for each window; leave it empty if a title would be redundant (Notes with a single window).
  - Don't title windows with your app name.
  - Write a concise title: a word or short phrase under 15 characters.
  - Use the standard Back and Close buttons with the standard symbols; don't use a text label that says Back or Close.
  - Provide actions that support the main tasks people perform, prioritizing the most frequent or most important commands.
  - Make sure the meaning of each control is clear; prefer simple, recognizable symbols instead of text, except for actions like edit that symbols don't represent well.
  - Prefer system-provided symbols without borders; the section provides the container and the system handles hover and selection states.
  - Use the `.prominent` style for key actions such as Done or Submit; only one primary action, on the trailing side.
  - Item groupings: Leading edge holds back-to-previous-document and sidebar toggles, then the view title and an optional document menu (Duplicate, Rename, Move, Export); leading items aren't customizable. Center area holds common controls (and the title if not leading), is customizable in macOS and iPadOS, and collapses into the overflow menu first. Trailing edge holds items that must remain available, inspector buttons, an optional search field, the More menu, and the primary action like Done; trailing items stay visible at all sizes.
  - Group toolbar items logically by function and frequency of use.
  - Group navigation controls and critical actions like Done, Close, or Save in dedicated, familiar, and visually distinct sections.
  - Keep consistent groupings and placement across platforms.
  - Minimize the number of groups; in general, aim for a maximum of three.
  - Keep actions with text labels separate from symbol actions and from each other by inserting fixed space.
- **Platform notes:**
  - tvOS: No additional considerations.
  - iOS: Prioritize only the most important items for inclusion in the main toolbar area and create a More menu for the rest. Use a large title to help people stay oriented; it transitions to a standard title when scrolling and back at the top.
  - iPadOS: Consider combining a toolbar with a tab bar in the same horizontal space at the top of the view.
  - macOS: The toolbar resides in the window frame below or integrated with the title bar; titles can be inline with controls and items don't include a bezel. Make every toolbar item available as a command in the menu bar, because people can customize or hide the toolbar.
  - visionOS: The system toolbar appears along the bottom edge of a window, above window-management controls, slightly in front along the z-axis, with a variable blur background. Items can carry a symbol or text label; looking at a symbol item reveals its text. Prefer using a system-provided toolbar. Avoid creating a vertical toolbar (tab bars are vertical). Try to prevent windows from resizing below the width of the toolbar. If your app can enter a modal state, consider offering contextually relevant toolbar controls and reinstate the standard ones afterward. Avoid using a pull-down menu in a toolbar, which may obscure the window controls below.
  - watchOS: Place toolbar buttons in the top corners or along the bottom; buttons above scrolling content remain visible. A scrolling toolbar button stays hidden until people scroll up. Use a scrolling toolbar button for an important action that isn't a primary app function (Mail's New Message at the top of the Inbox).
- **Content/labels:** Title under 15 characters, never the app name; symbols preferred over text; standard symbols for Back and Close; "edit" is an example where text beats a symbol.
- **APIs:** Toolbars, `ScrollEdgeEffectStyle`, `ToolbarItemPlacement.topBarLeading`, `.topBarTrailing`, `.bottomBar`, `.primaryAction` (SwiftUI); `UIToolbar`, `UIBarButtonItem.SystemItem.fixedSpace`, `UINavigationBar.prefersLargeTitles` (UIKit); `NSToolbar` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A `<header role="toolbar">` with leading (back, sidebar toggle, `<h1>` title), center, and trailing groups separated by flex gaps; icon buttons carry `aria-label`; collapse the center group into a "More" `role="menu"` at narrow widths; add a backdrop blur or shadow only when content scrolls beneath.
- **Source:** [reference](../references/components/menus-and-actions/toolbars.md)

---

## Navigation and search

### Path controls
- **What it is:** A path control shows the file system path of a selected file or folder.
- **Platforms:** macos
- **Use it when:**
  - People need to see (and optionally navigate) the location of a selected item, like the Finder's path bar shown with View > Show Path Bar.
  - You want the standard style (a linear list of root disk, parent folders, and selected item with icons) or the pop up style (a pop-up-button-like control that reveals the hierarchy in a menu, with a Choose command when editable).
- **Don't use it when / use instead:**
  - You want to place it in a toolbar or status bar; it belongs in the window body.
  - You need a general mutually exclusive choice; use a [Pop-up button](../references/components/menus-and-actions/pop-up-buttons.md).
- **Rules:**
  - Use a path control in the window body, not the window frame; the Finder's path control appears at the bottom of the window body, not in the status bar.
  - Standard style: if the list is too long, the control hides names between the first and last items; editable controls accept dropped items.
  - Pop up style: shows the selected item's icon and name; the menu lists root disk, parent folders, and selected item, plus Choose when editable.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Content/labels:** Each item shows an icon and a name.
- **APIs:** `NSPathControl` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A breadcrumb `<nav aria-label="Path"><ol>` of links with icons, collapsing middle items into an ellipsis when space is short; place it in the content area, not the app header.
- **Source:** [reference](../references/components/navigation-and-search/path-controls.md)

### Search fields
- **What it is:** A search field lets people search a collection of content for specific terms they enter.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - People need to find specific content in a collection, with a Search icon, a Clear button, and placeholder text.
  - You want to narrow searches with a scope bar (filter among clearly defined categories) or tokens (selectable, editable search terms).
- **Don't use it when / use instead:**
  - You're tokenizing arbitrary entries like recipients on macOS; use [Token fields](../references/components/navigation-and-search/token-fields.md).
  - A small, visible set of filters is enough; a scope bar or [Segmented control](../references/components/selection-and-input/segmented-controls.md) may do.
- **Rules:**
  - Use placeholder text to help people know what they can search for.
  - If possible, start search immediately when a person types.
  - Consider showing suggested search terms (recent searches before typing, predictive suggestions while typing).
  - Simplify search results; show the most relevant first and consider categorizing them.
  - Consider letting people filter search results, for example with a scope bar in the results area.
  - Use a scope bar to filter among clearly defined search categories.
  - Default to a broader scope and let people refine it as they need.
  - Use tokens to filter by common search terms or items (a specific contact in Mail, photos in Messages).
  - Consider pairing tokens with search suggestions so people learn which tokens exist.
- **Platform notes:**
  - visionOS: No additional considerations.
  - iOS: Three entry points: a tab in the tab bar, a toolbar at the bottom or top, or inline with content. Search as a tab has two styles: Standard tab (navigates to a search landing page) and Button appearance (immediately focuses the field and shows the keyboard). Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration (Apple TV). Choose the button appearance to help people quickly find what they need. Search in a toolbar: Place search at the bottom if there's room (Settings, Mail, Notes). Place search at the top when it's important to defer to content at the bottom of the screen, or there's no bottom toolbar (Wallet). Search as an inline field: Place search as an inline field when its position alongside the content it searches strengthens that relationship (Music library filter). When at the top, position an inline search field above the list it searches, and consider pinning it to the top toolbar when scrolling.
  - iPadOS, macOS: Keep the search experience consistent across both platforms. Put a search field at the trailing side of the toolbar for many common uses (Mail, Notes, Voice Memos, Freeform). Include search at the top of the sidebar when filtering content or navigation there (Settings). Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery (Music, TV). In a search field in a dedicated area, consider immediately focusing the field when a person navigates to the area, except on iPad when only a virtual keyboard is available. Account for window resizing with the placement of the search field; in compact views place search above the content list column (Notes, Mail).
  - tvOS: A search screen is a specialized keyboard screen with results beneath. Provide suggestions to make searching easier, including popular, context-specific, and recent searches.
  - watchOS: Tapping the search field shows a full-screen text-input control; the app returns to the field after Cancel or Search.
- **Content/labels:** Placeholder text reinforces the scope or the type of content searched.
- **APIs:** `searchable(text:placement:prompt:)`, Adding a search interface to your app, Scoping a search operation (SwiftUI); `UISearchBar`, `UISearchTextField`, `UISearchController` (UIKit); `NSSearchField` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<form role="search">` with `<input type="search">` (gives a native Clear button), `placeholder`, a visible or visually hidden `<label>`, live results in an `aria-live` region or `role="listbox"` suggestions, and scope filters as a `role="radiogroup"`; tokens as removable chips inside the field.
- **Source:** [reference](../references/components/navigation-and-search/search-fields.md)

### Sidebars
- **What it is:** A sidebar appears on the leading side of a view and lets people navigate between areas of your app or top-level collections of content, like folders and playlists.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **Use it when:**
  - You have a large amount of vertical and horizontal space and many top-level areas or collections to navigate.
  - People benefit from customizing which areas appear and in what order.
- **Don't use it when / use instead:**
  - Space is limited or you want to devote more of the screen to content; a [Tab bar](../references/components/navigation-and-search/tab-bars.md) (or a tab bar that adapts to a sidebar) is more compact.
  - Your hierarchy is deeper than two levels; use a [Split view](../references/components/layout-and-organization/split-views.md) with a content list between sidebar and detail.
  - You target watchOS; sidebars aren't supported.
- **Rules:**
  - Extend visually rich content beneath the sidebar, by horizontal scrolling or a background extension effect, to reinforce the Liquid Glass layer separation.
  - When possible, let people customize the contents of a sidebar.
  - Group hierarchy with disclosure controls if your app has a lot of content.
  - Consider using familiar symbols to represent items in the sidebar; prefer a custom symbol over a bitmap if you need a custom icon.
  - Consider letting people hide the sidebar using platform interactions (edge swipe on iPadOS, show/hide button or View menu commands on macOS); avoid hiding the sidebar by default.
  - In general, show no more than two levels of hierarchy in a sidebar.
  - If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group.
  - Make sure any sidebar icon colors you choose serve a clear purpose; by default icons use the app accent color, and on macOS they must follow the system accent color people choose. Use fixed colors sparingly (Mail's yellow VIP icon).
- **Platform notes:**
  - tvOS: No additional considerations. Not supported in watchOS.
  - iOS, iPadOS: The `sidebarAdaptable` tab view style lets you choose whether a sidebar or tab bar appears at launch, with a button to switch; it adapts to rotation and window resizing. For a sidebar only, use `NavigationSplitView` or `UISplitViewController`. Consider using a tab bar first; use the convertible sidebar for less frequently used areas. If necessary, apply the correct sidebar appearance with `UICollectionLayoutListConfiguration.Appearance.sidebar` when not using SwiftUI.
  - macOS: Row height, text, and glyph size depend on the small, medium, or large sidebar size, which people can change in General settings. Consider automatically hiding and revealing a sidebar when its container window resizes. Avoid putting critical information or actions at the bottom of a sidebar, because people often hide the bottom edge of a window.
  - visionOS: If your app's hierarchy is deep, consider using a sidebar within a tab in a tab bar for secondary navigation, and prevent sidebar selections from changing the current tab. Windows typically expand to fit a sidebar, so hiding it is rare.
- **Content/labels:** Group titles short and descriptive; omit unnecessary words.
- **APIs:** `sidebarAdaptable`, `NavigationSplitView`, `ListStyle.sidebar`, `backgroundExtensionEffect()` (SwiftUI); `UICollectionLayoutListConfiguration`, `UISplitViewController` (UIKit); `NSSplitViewController` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<nav aria-label="Sections">` on the leading side containing grouped `<ul>` lists with `aria-current="page"` on the active link and `<details>` for collapsible groups; collapse to a tab bar or drawer below a compact breakpoint; keep nothing critical pinned to the bottom.
- **Source:** [reference](../references/components/navigation-and-search/sidebars.md)

### Tab bars
- **What it is:** A tab bar lets people navigate between top-level sections of your app.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **Use it when:**
  - People need to switch between distinct sections of an app (Clock: Alarm, Stopwatch, Timer) while preserving each section's navigation state.
  - You want navigation that stays visible and takes little space.
- **Don't use it when / use instead:**
  - You need controls that act on elements in the current view; use a [Toolbar](../references/components/menus-and-actions/toolbars.md).
  - You're switching between closely related subviews on iOS; use a [Segmented control](../references/components/selection-and-input/segmented-controls.md).
  - Your information structure is complex; consider a [Sidebar](../references/components/navigation-and-search/sidebars.md) or a tab bar that adapts to one.
- **Rules:**
  - Use a tab bar to support navigation, not to provide actions.
  - Make sure the tab bar is visible when people navigate to different sections of your app; only a temporary modal view may cover it.
  - Use the appropriate number of tabs required to help people navigate your app; fewer tabs are easier.
  - Avoid overflow tabs; the trailing tab becomes a More tab in iOS and iPadOS, which hides content.
  - Don't disable or hide tab bar buttons, even when their content is unavailable; explain why a section is empty instead.
  - Include tab labels to help with navigation; use single words whenever possible.
  - Consider using SF Symbols for familiar, scalable icons; prefer filled symbols. Icons sit above labels in compact views and beside them in regular views.
  - Use a badge (a red oval with white text, a number or an exclamation point) only to indicate that critical information is available.
  - Avoid applying a similar color to tab labels and content layer backgrounds; prefer a monochromatic appearance or a sufficiently distinct accent color.
- **Platform notes:**
  - macOS: No additional considerations. Not supported in watchOS.
  - iOS: The tab bar floats above content at the bottom on a Liquid Glass background. With an attached accessory (Music's MiniPlayer), you can minimize the tab bar and move the accessory inline on scroll; tapping a tab or scrolling to the top exits the minimized state. A dedicated search tab can sit at the trailing end.
  - iPadOS: The tab bar appears near the top of the screen, fixed or with a button to convert it to a sidebar. Prefer a tab bar for navigation; offer the sidebar conversion for more complex apps. Let people customize the tab bar; if you do, aim for a default list of five or fewer. Use a navigation split view for a sidebar that can't convert to a tab bar.
  - tvOS: Highly customizable (background tint or image, fonts, item tints, extra button icons). Translucent by default with only the selected tab opaque; the tab bar height is 68 points and its top edge is 46 points from the top of the screen, neither changeable. Overflowing items fade and truncate. Be aware of tab bar scrolling behaviors: the bar scrolls offscreen when a tab has a single main view but stays pinned with a split view, and Menu on the remote returns focus to it. In a live-viewing app, organize tabs as Live content, Cloud DVR or other recorded content, Other content.
  - visionOS: The tab bar is always vertical on the window's leading side and expands when looked at, possibly obscuring content. Supply a symbol and a text label for each tab and keep labels short. If it makes sense, consider using a sidebar within a tab for deep hierarchies, without letting sidebar selections change the tab.
- **Content/labels:** Single-word labels when possible; filled SF Symbols; badges reserved for critical information.
- **APIs:** `TabView`, `TabViewBottomAccessoryPlacement`, `TabBarMinimizeBehavior`, `tabBarOnly`, `sidebarAdaptable`, `TabViewCustomization` (SwiftUI); `UITabBar`, `UITabBarController.MinimizeBehavior`, `UITab.Placement` (UIKit).
- **Web equivalent (translation, not Apple guidance):** A fixed-bottom (mobile) or top (wide) `<nav>` of links, each with an icon plus one-word label and `aria-current="page"` on the active section; never disable or hide a section link; badges as a small `aria-label`ed count; switch to a sidebar layout above a breakpoint rather than adding a "More" overflow.
- **Source:** [reference](../references/components/navigation-and-search/tab-bars.md)

### Token fields
- **What it is:** A token field is a type of text field that can convert text into tokens that are easy to select and manipulate.
- **Platforms:** macos
- **Use it when:**
  - People enter multiple discrete values like recipients, and each should become a selectable, draggable token (Mail's address fields).
  - You can suggest values as people type and offer per-token information or editing through a contextual menu.
- **Don't use it when / use instead:**
  - You need search filter tokens on other platforms; see [Search fields](../references/components/navigation-and-search/search-fields.md).
  - A single plain value is enough; use a [Text field](../references/components/selection-and-input/text-fields.md).
- **Rules:**
  - Add value with a context menu offering additional options or information about a token.
  - Consider providing additional ways to convert text into tokens; by default text becomes a token when people type a comma, and you can add shortcuts like Return.
  - Consider customizing the delay the system uses before showing suggested tokens; suggestions appear immediately by default, which can distract.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, visionOS, and watchOS.
- **Content/labels:** Tokens represent the entered item (for example a recipient's name).
- **APIs:** `NSTokenField` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A chip input: an editable `<input role="combobox" aria-autocomplete="list">` inside a container of removable chip `<span>`s or buttons; convert on comma and Enter, offer suggestions in a `role="listbox"` after a short delay, and give each chip a context menu or remove action.
- **Source:** [reference](../references/components/navigation-and-search/token-fields.md)

---

## Presentation

### Action sheets
- **What it is:** An action sheet is a modal view that presents choices related to an action people initiate.
- **Platforms:** ios, ipados, macos, tvos, watchos
- **Use it when:**
  - People just initiated an intentional action that needs clarifying choices (cancel a Mail draft: delete or save).
  - You need to confirm a destructive choice from a pull-down menu item (iOS).
- **Don't use it when / use instead:**
  - You need to interrupt with critical information or confirm a single destructive action without extra choices; use an [Alert](../references/components/presentation/alerts.md).
  - People expect to reveal choices themselves; use a [Menu](../references/components/menus-and-actions/menus.md).
  - You target visionOS; action sheets aren't supported.
- **Rules:**
  - Use an action sheet, not an alert, to offer choices related to an intentional action.
  - Use action sheets sparingly; they interrupt the current task.
  - Aim to keep titles short enough to display on a single line.
  - Provide a message only if necessary; the title and context usually suffice.
  - If necessary, provide a Cancel button that lets people reject an action that might destroy data; place it at the bottom (upper-left corner in watchOS). A SwiftUI confirmation dialog includes Cancel by default.
  - Make destructive choices visually prominent with the destructive style and place them at the top of the action sheet.
- **Platform notes:**
  - macOS, tvOS: No additional considerations. Not supported in visionOS.
  - iOS, iPadOS: Use an action sheet, not a menu, to provide choices related to an action. Avoid letting an action sheet scroll; more buttons mean more effort and accidental taps.
  - watchOS: The system style includes a title, optional message, a Cancel button, and one or more additional buttons, with three button styles: Default (no special meaning), Destructive (destroys data or performs a destructive action), Cancel (dismisses without action). Avoid displaying more than four buttons in an action sheet, including the Cancel button, so no more than three additional choices.
- **Content/labels:** Single-line title; message only when needed; destructive buttons styled red.
- **APIs:** `confirmationDialog(_:isPresented:titleVisibility:actions:)`, `ButtonRole.destructive` (SwiftUI); `UIAlertController.Style.actionSheet`, `UIAlertAction.Style.destructive` (UIKit).
- **Web equivalent (translation, not Apple guidance):** A modal `<dialog>` anchored to the bottom on small screens listing choices as full-width buttons (destructive first and styled as danger, Cancel last), triggered only right after a user action; close on Escape and Cancel.
- **Source:** [reference](../references/components/presentation/action-sheets.md)

### Alerts
- **What it is:** An alert gives people critical information they need right away.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You must tell people about a problem, warn them that an action might destroy data, or let them confirm a purchase or other important action they initiated.
  - People took an uncommon destructive action they can't undo, and it might have been accidental.
- **Don't use it when / use instead:**
  - You only need to provide information; communicate it within the relevant context (Mail shows an indicator when a server is unavailable).
  - The action is common and undoable (deleting an email or file), even if destructive.
  - People need extra choices related to an intentional action; use an [Action sheet](../references/components/presentation/action-sheets.md).
  - The app is starting up; design a discoverable way to present the information instead.
  - You want to notify about something outside the app; a [Notification](../references/components/system-experiences/notifications.md) is not for errors, but an alert is not for background news either.
- **Rules:**
  - Use alerts sparingly; each one offers only essential information and useful actions.
  - Avoid using an alert merely to provide information.
  - Avoid displaying alerts for common, undoable actions, even when they're destructive.
  - Avoid showing an alert when your app starts.
  - An alert displays a title, optional informative text, and up to three buttons; iOS, iPadOS, macOS, and visionOS alerts can include a text field; macOS and visionOS can include an icon and accessory view; macOS can add a suppression checkbox and a Help button.
  - In all alert copy, be direct, and use a neutral, approachable tone.
  - Write a title that clearly and succinctly describes the situation; avoid "Error" or "Error 329347 occurred" and avoid titles that wrap to more than two lines.
  - Include informative text only if it adds value, keeping it short.
  - Avoid explaining alert buttons; if you must, use a term like choose and refer to the button by its exact title without quotes.
  - If supported, include a text field only if you need people's input to resolve the situation (for example a secure field for a password).
  - Create succinct, logical button titles: one or two words, verbs or verb phrases related to the alert ("View All", "Reply", "Ignore"); "OK" only in informational alerts, never "Yes" and "No"; always "Cancel" for the cancel button.
  - Avoid using OK as the default button title unless the alert is purely informational; prefer specific titles like "Erase", "Convert", "Clear", "Delete".
  - Place buttons where people expect: the most likely button on the trailing side of a row or at the top of a stack; the default button always trailing or top; Cancel typically leading or bottom.
  - Use the destructive style to identify a button that performs a destructive action people didn't deliberately choose; a deliberately chosen action like Empty Trash doesn't get the destructive style.
  - If there's a destructive action, include a Cancel button; never make Cancel the default. To encourage reading, avoid making any button the default. A single default button should be Done, not Cancel.
  - Provide alternative ways to cancel an alert when it makes sense: exit to the Home Screen (iOS, iPadOS); Escape or Command-Period on a keyboard (iOS, iPadOS, macOS, visionOS); Menu on the remote (tvOS).
- **Platform notes:**
  - tvOS, watchOS: No additional considerations.
  - iOS, iPadOS: Use an action sheet, not an alert, to offer choices related to an intentional action. When possible, avoid displaying an alert that scrolls; keep titles short and messages brief.
  - macOS: The app icon appears automatically (an alternative icon or symbol is allowed); you can configure repeating alerts with a suppression option, append an accessory view, and include a Help button. Use a caution symbol (`exclamationmark.triangle`) sparingly, only when extra attention is really needed, never for tasks whose only purpose is to overwrite or remove data like save or empty trash.
  - visionOS: In the Shared Space the alert appears in front of the app's window, slightly forward along the z-axis, and stays anchored if the window moves; in a Full Space it's centered in the field of view. An accessory view has a maximum height of 154 pt and a 16-pt corner radius.
- **Content/labels:** Title: sentence-style capitalization with ending punctuation if a complete sentence; title-style capitalization without punctuation if a fragment. Informative text: complete sentences, sentence-style capitalization, punctuation. Buttons: title-style capitalization, no ending punctuation.
- **APIs:** `alert(_:isPresented:actions:)` (SwiftUI); `UIAlertController` (UIKit); `NSAlert`, `NSAlert.accessoryView` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<dialog role="alertdialog" aria-labelledby aria-describedby>` opened with `showModal()`, up to three buttons with the primary last in the row and Cancel first, no `autofocus` on a destructive button, Escape cancels; never use it for passive information or at page load.
- **Source:** [reference](../references/components/presentation/alerts.md)

### Page controls
- **What it is:** A page control displays a row of indicator images, each of which represents a page in a flat list.
- **Platforms:** ios, ipados, tvos, visionos, watchos
- **Use it when:**
  - People move between an ordered list of peer pages (Weather locations), including lists people create themselves.
  - A scroll view is in page-by-page mode and needs an indicator.
- **Don't use it when / use instead:**
  - Page relationships are hierarchical or nonsequential; use a [Sidebar](../references/components/navigation-and-search/sidebars.md) or [Split view](../references/components/layout-and-organization/split-views.md).
  - You have more than about 10 pages as peers; use a different arrangement such as a grid.
  - You target macOS; page controls aren't supported.
- **Rules:**
  - Use page controls to represent movement between an ordered list of pages.
  - Center a page control at the bottom of the view or window.
  - Although page controls can handle any number of pages, don't display too many; more than about 10 dots are hard to count at a glance.
  - Make sure custom indicator images are simple and clear; avoid complex shapes, negative space, text, or inner lines.
  - Customize the default indicator image only when it enhances the page control's overall meaning (for example `bookmark.fill` when every page holds bookmarks).
  - Avoid using more than two different indicator images in a page control (Weather uses `location.fill` for the current location and dots elsewhere).
  - Avoid coloring indicator images; let the system color them.
- **Platform notes:**
  - Not supported in macOS.
  - iOS, iPadOS: The control highlights the current indicator and can shrink indicators at both sides when more pages exist. People tap the leading or trailing side for next or previous (and target indicators with the pointer on iPadOS) or scrub by dragging. Avoid animating page transitions during scrubbing; use the animated transition only for tapping. Background styles: Automatic (background only during interaction; use when the control isn't the primary navigation element), Prominent (always; only when it's the primary navigational control), Minimal (never; just to show position). Avoid supporting the scrubber when you use the minimal background style.
  - tvOS: Use page controls on collections of full-screen pages; additional controls make it hard to maintain focus.
  - visionOS: Page controls represent and indicate pages, but people don't interact with them.
  - watchOS: Page controls appear at the bottom for horizontal pagination, or next to the Digital Crown for a vertical tab view, where the indicator shows position within the page and within the set. Use vertical pagination to separate multiple views into distinct, purposeful pages. Consider limiting the content of an individual page to a single screen height, placing variable-height pages after fixed-height ones.
- **Content/labels:** None beyond indicator imagery.
- **APIs:** `PageTabViewStyle` (SwiftUI); `UIPageControl`, `preferredIndicatorImage`, `setIndicatorImage(_:forPage:)`, `UIPageControl.InteractionState`, `backgroundStyle` (UIKit).
- **Web equivalent (translation, not Apple guidance):** A centered `role="tablist"` of small dot buttons (`role="tab"`, `aria-selected`, `aria-label="Page n of N"`) below a `scroll-snap-type: x mandatory` carousel; cap at about 10 dots and leave dot colors to a single system pair.
- **Source:** [reference](../references/components/presentation/page-controls.md)

### Panels
- **What it is:** In a macOS app, a panel typically floats above other open windows providing supplementary controls, options, or information related to the active window or current selection.
- **Platforms:** macos
- **Use it when:**
  - People need quick access to important controls or information related to the content they're working with (settings for the selected item).
  - You're presenting an inspector whose contents update as the selection changes.
  - People need to repeatedly provide input and observe results (find and replace), which a sheet can't support.
- **Don't use it when / use instead:**
  - You need an Info window whose contents stay the same regardless of selection; use a regular [Window](../references/components/presentation/windows.md).
  - You're on another platform; use a modal view such as a [Sheet](../references/components/presentation/sheets.md), or a [Split view](../references/components/layout-and-organization/split-views.md) pane for an inspector.
  - You'd use a HUD without a media-oriented reason; prefer standard panels.
- **Rules:**
  - Use a panel to give people quick access to important controls or information related to the content they're working with.
  - Consider using a panel to present inspector functionality.
  - Prefer simple adjustment controls in a panel, such as sliders and steppers, over typing or selecting items.
  - Write a brief title that describes the panel's purpose, because a floating panel needs a title bar for positioning.
  - Show and hide panels appropriately: bring all open panels forward when the app becomes active; hide them when it's inactive.
  - Avoid including panels in the Window menu's documents list (show/hide commands are fine).
  - In general, avoid making a panel's minimize button available.
  - Refer to panels by title in your interface and in help documentation.
  - HUD-style panels: Prefer standard panels; use a HUD only in a media-oriented app, when a standard panel would obscure essential content, or when you don't need controls beyond a disclosure triangle. Maintain one panel style when your app switches modes. Use color sparingly in HUDs. Keep HUDs small and don't let them obscure the content they adjust.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Content/labels:** Titles are nouns or noun phrases with title-style capitalization ("Fonts", "Colors", "Inspector"). In menus use the title without the word panel ("Show Fonts", "Show Inspector"); in documentation refer to the title or append window ("Fonts window").
- **APIs:** `NSPanel`, `NSWindow.StyleMask.hudWindow` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A non-modal `<dialog>` (opened with `show()`, not `showModal()`) or a floating `<section role="complementary">` with a draggable title bar, positioned `fixed` above the document, holding sliders and steppers; hide it when the app loses focus.
- **Source:** [reference](../references/components/presentation/panels.md)

### Popovers
- **What it is:** A popover is a transient view that appears above other content when people click or tap a control or interactive area.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - You want to expose a small amount of information or functionality related to a control (a calendar event's date, time, or calendar).
  - You need content only temporarily and want to avoid the space a sidebar or panel takes.
- **Don't use it when / use instead:**
  - You're in a compact view (iPhone); present information in a full-screen modal view like a [Sheet](../references/components/presentation/sheets.md).
  - You need to warn people; use an [Alert](../references/components/presentation/alerts.md), because people can miss or accidentally close a popover.
  - You need to show a menu from a macOS menu bar extra; show a menu, not a popover.
  - You target tvOS or watchOS; popovers aren't supported.
- **Rules:**
  - Use a popover to expose a small amount of information or functionality; limit it to a few related tasks.
  - Consider using popovers when you want more room for content than a menu offers but only temporarily.
  - Position popovers appropriately; the arrow points as directly as possible at the revealing element and the popover avoids covering it or essential content.
  - Use a Close button for confirmation and guidance only (Cancel or Done when it clarifies saving); otherwise the popover closes when people click or tap outside or select an item. With multiple selections, keep it open until explicit dismissal or an outside tap.
  - Always save work when automatically closing a nonmodal popover; discard only on an explicit Cancel.
  - Show one popover at a time; never cascade popovers; close the open one before showing a new one.
  - Don't show another view over a popover, except an alert.
  - When possible, let people close one popover and open another with a single click or tap.
  - Avoid making a popover too big; only big enough for its contents and arrow.
  - Provide a smooth transition when changing the size of a popover; animate between condensed and expanded views.
  - Avoid using a popover to show a warning.
- **Platform notes:**
  - visionOS: No additional considerations. Not supported in tvOS or watchOS.
  - iOS, iPadOS: Avoid displaying popovers in compact views; adjust layout by size class and use a sheet in compact widths.
  - macOS: You can make a popover detachable so it becomes a separate panel when dragged. Consider letting people detach a popover. Make minimal appearance changes to a detached popover so people keep context.
- **Content/labels:** Avoid using the word popover in help documentation; refer to the task or selection instead ("Select the Show button").
- **APIs:** `popover(isPresented:attachmentAnchor:arrowEdge:content:)` (SwiftUI); `UIPopoverPresentationController` (UIKit); `NSPopover` (AppKit).
- **Web equivalent (translation, not Apple guidance):** The HTML `popover` attribute (or a non-modal `<dialog>`) anchored to its trigger (`aria-haspopup="dialog"`, `aria-expanded`), with a CSS arrow pointing at the trigger, light-dismiss on outside click and Escape, one open at a time, and automatic saving on dismiss; on narrow viewports render the same content as a bottom sheet.
- **Source:** [reference](../references/components/presentation/popovers.md)

### Scroll views
- **What it is:** A scroll view lets people view content that's larger than the view's boundaries by moving the content vertically or horizontally.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - Content extends beyond the visible area and people need to move through it.
  - You want page-by-page scrolling by a fixed amount, optionally with an overlap unit.
- **Don't use it when / use instead:**
  - You'd nest a scroll view inside another with the same orientation; that's unpredictable (perpendicular nesting is fine).
  - You need a flat set of pages with a position indicator; add a [Page control](../references/components/presentation/page-controls.md) or, on watchOS, use a [Tab view](../references/components/layout-and-organization/tab-views.md).
- **Rules:**
  - Support default scrolling gestures and keyboard shortcuts; custom scrolling must keep the elastic behavior people expect.
  - Make it apparent when content is scrollable, for example by showing partial content at the edge.
  - Avoid putting a scroll view inside another scroll view with the same orientation.
  - Consider supporting page-by-page scrolling if it makes sense for your content, defining a page as the view's height or width and subtracting an overlap unit.
  - In some cases, scroll automatically to help people find their place: when the app selects or places the insertion point in hidden content, when people start typing in an offscreen location, when the pointer moves past the edge during selection, or when people act on a selection they scrolled away from; scroll only as much as necessary.
  - If you support zoom, set appropriate maximum and minimum scale values.
  - Prefer the automatic scroll edge effect style; test thoroughly if you use the soft style.
  - Only use a scroll edge effect when a scroll view is behind floating interface elements; it isn't decorative.
  - Apply one scroll edge effect per view; in split views each pane can have its own, kept consistent in height.
- **Platform notes:**
  - iOS, iPadOS: Consider showing a page control when a scroll view is in page-by-page mode, and don't show the scroll indicator on the same axis.
  - macOS: A scroll indicator is commonly called a scroll bar. If necessary, use small or mini scroll bars in a panel, matching the size of other controls there.
  - tvOS: Views scroll but aren't distinct objects with indicators; the system scrolls to keep focused items visible.
  - visionOS: The indicator is small and fixed in size, vertically centered at the trailing edge or horizontally centered at the bottom; looking at it and dragging enables a jog bar with tick marks for speed control. If necessary, account for the size of the scroll indicator by increasing tight margins. Look to Scroll: Support Look to Scroll for reading or browsing views (it's opt-in per scroll view). Avoid using Look to Scroll for secondary content with controls or dense information. Maintain consistency across content (support it in all similar views). Define clear scroll areas within your app, preferring full width or height of the window. If your app uses custom scroll effects or animations, remove them before supporting Look to Scroll.
  - watchOS: Prefer vertically scrolling content navigated with the Digital Crown. Use tab views to provide page-by-page scrolling. When displaying paged content, consider limiting the content of an individual page to a single screen height, placing variable-height pages after fixed-height ones.
- **Content/labels:** None given.
- **APIs:** `ScrollView`, `PagingScrollTargetBehavior`, `ScrollEdgeEffectStyle`, `ScrollInputKind.look` (SwiftUI); `UIScrollView`, `UIScrollEdgeEffect.Style` (UIKit); `NSScrollView`, `NSScrollEdgeEffectStyle` (AppKit); `WKPageOrientation` (WatchKit).
- **Web equivalent (translation, not Apple guidance):** A container with `overflow: auto` and `overscroll-behavior` left at default; `scroll-snap-type` for page-by-page; `scrollIntoView({block: "nearest"})` for minimal automatic scrolling; avoid nested same-axis scrollers; add a top-edge blur or shadow only under a sticky header.
- **Source:** [reference](../references/components/presentation/scroll-views.md)

### Sheets
- **What it is:** A sheet helps people perform a scoped task that's closely related to their current context.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You need specific information from people or want to present a simple task they complete before returning to the parent view (attach a file, choose a save location).
  - On iOS or iPadOS you want a nonmodal sheet that affects the parent view while staying visible (Notes' format sheet).
- **Don't use it when / use instead:**
  - The flow is complex or prolonged; use a full-screen modal view (iOS, iPadOS), a new window or full-screen mode (macOS), or a Full Space (visionOS).
  - People need to repeatedly provide input and observe results on macOS; use a [Panel](../references/components/presentation/panels.md).
  - You need to present important information or a set of choices on watchOS; use an [Alert](../references/components/presentation/alerts.md) or [Action sheet](../references/components/presentation/action-sheets.md).
  - You need supplementary items in visionOS; use a [Split view](../references/components/layout-and-organization/split-views.md).
- **Rules:**
  - For complex or prolonged user flows, consider alternatives to sheets.
  - Display only one sheet at a time from the main interface; close the first before showing a second, then optionally show the first again.
  - Use a nonmodal view when you want to present supplementary items that affect the main task in the parent view.
  - Provide an alternative to the Done button: always pair Done with Cancel (or Back in a multistep flow); never rely on Done alone.
  - Avoid showing all three buttons (Cancel, Done, and Back) together.
  - Cancel (or Close) dismisses without saving; Done dismisses after completing or saving; Back moves to a previous step and isn't meant to dismiss.
- **Platform notes:**
  - tvOS: No additional considerations.
  - iOS, iPadOS: Cancel belongs on the leading edge of the top toolbar and Done on the trailing edge. Multistep flows: first step shows Cancel leading and an inactive Done trailing; subsequent steps replace Cancel with Back; the final step activates Done. Resizable sheets rest at detents: large (fully expanded) and medium (about half); sheets support large automatically, and specifying only medium prevents full height. In an iPhone app, consider supporting the medium detent for progressive disclosure (share sheet), but not when content needs full height (Messages and Mail compose). Include a grabber in a resizable sheet; it signals resizing, cycles detents on tap, and works with VoiceOver. Support swiping to dismiss a sheet; confirm unsaved changes with an action sheet. Prefer using the page or form sheet presentation styles in an iPadOS app.
  - macOS: A cardlike view with rounded corners floating over a dimmed parent window; people can still use other app windows. Present a sheet in a reasonable default size and consider supporting resizing. Let people interact with other app windows without first dismissing a sheet. Use a panel instead of a sheet if people need to repeatedly provide input and observe results.
  - visionOS: The sheet floats in front of its dimmed parent window. Avoid displaying a sheet that emerges from the bottom edge of a window; center it in the field of view. Present a sheet in a default size that helps people retain their context, not covering most of the window, and consider allowing resizing.
  - watchOS: A full-screen semitransparent view over blurred, desaturated content. Use a sheet only when your modal task requires a custom title or custom content presentation. Keep sheet interactions brief and occasional; don't use a sheet for navigation. If you change the default label, prefer using SF Symbols to represent the action, and avoid labels that look like a Back button or a page title.
- **Content/labels:** Button titles Cancel, Done, Back; on watchOS the default Cancel label is preferred over custom text.
- **APIs:** `sheet(item:onDismiss:content:)` (SwiftUI); `UISheetPresentationController`, `detents`, `prefersGrabberVisible`, `UIModalPresentationStyle`, `UIModalPresentationStyle.fullScreen` (UIKit); `presentAsSheet(_:)` (AppKit, `NSViewController`).
- **Web equivalent (translation, not Apple guidance):** A modal `<dialog>` (bottom sheet on narrow screens, centered card on wide) with a header holding Cancel (leading) and Done (trailing); support drag-to-resize snap points via `scroll-snap` or pointer events and a visible grabber; never stack two sheets; confirm discarding unsaved changes.
- **Source:** [reference](../references/components/presentation/sheets.md)

### Windows
- **What it is:** A window presents UI views and components in your app or game.
- **Platforms:** ipados, macos, visionos
- **Use it when:**
  - You need a primary window for main navigation and content, or an auxiliary window dedicated to one task or area with a close button.
  - Opening content separately helps people multitask or preserve context (Mail's Compose window).
- **Don't use it when / use instead:**
  - You'd open new windows as default behavior without benefit; that creates clutter.
  - You need supplementary info in visionOS; prefer a [Split view](../references/components/layout-and-organization/split-views.md).
  - You need a floating helper on macOS; use a [Panel](../references/components/presentation/panels.md).
- **Rules:**
  - Make sure that your windows adapt fluidly to different sizes to support multitasking and multiwindow workflows.
  - Choose the right moment to open a new window; avoid opening new windows as default behavior unless it makes sense.
  - Consider providing the option to view content in a new window via a context menu or File menu command.
  - Avoid creating custom window UI; don't replicate system frames or controls.
  - Use the term window in user-facing content, not scene.
- **Platform notes:**
  - Not supported in iOS, tvOS, or watchOS.
  - iPadOS: Windows present full screen or windowed depending on Multitasking & Gestures settings; windowed apps are freely resizable and the system remembers size and placement. Make sure window controls don't overlap toolbar items; move leading toolbar buttons inward when window controls appear. Consider letting people use a gesture to open content in a new window (pinch in Notes). You can present a single file without creating your own window but must support multiple windows.
  - macOS: A window has a frame (window controls, toolbar, rarely a bottom bar) and a body area. States: Main (frontmost, one per app), Key (accepts input, one onscreen at a time, colored title bar controls), Inactive (gray controls, no vibrancy). Make sure custom windows use the system-defined appearances for each state. Avoid putting critical information or actions in a bottom bar; use it only for a small amount of information like Finder's status bar, otherwise use an inspector.
  - visionOS: Two styles: default window (glass background, close button, window bar, resize controls, optional Share button, tab bar, toolbar, ornaments) and volumetric window (volume) for 3D content; a plain style omits the glass. Prefer using a window to present a familiar interface and to support familiar tasks. Retain the window's glass background. Choose an initial window size that minimizes empty areas; the default is 1280x720 pt, placed about two meters in front of the wearer with an apparent width of about three meters. Aim for an initial shape that suits a window's content. Choose a minimum and maximum size for each window. Minimize the depth of 3D content you display in a window; use a volume for deeper content. Volumes: Prefer using a volume to display rich, 3D content. Place 2D content so it looks good from multiple angles, using attachments. In general, use dynamic scaling (fixed scaling for real-world-sized objects). Take advantage of the default baseplate appearance (glow on look in visionOS 2 and later). Consider offering high-value content in an ornament anchored like `topBack` or `bottomFront`, not on the same edge as a toolbar or tab bar, and prefer only one extra ornament. Choose an alignment that supports the way people interact with your volume (parallel to the floor for passive content, tilting toward the viewer for interactive content).
- **Content/labels:** Say window, never scene.
- **APIs:** Windows, `WindowGroup`, `OpenWindowAction`, `DefaultWindowStyle`, `VolumetricWindowStyle`, `PlainWindowStyle`, `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)` (SwiftUI); `UIWindow`, `UIWindowScene.ActivationInteraction`, `collectionView(_:sceneActivationConfigurationForItemAt:point:)`, `QLPreviewSceneActivationConfiguration` (UIKit, QuickLook); `NSWindow` (AppKit).
- **Web equivalent (translation, not Apple guidance):** The browser tab or window is the primary window; open auxiliary content with `window.open` or `target="_blank"` only on explicit user request, never by default; use responsive layout (container queries) so content adapts to any size, and never draw fake window chrome.
- **Source:** [reference](../references/components/presentation/windows.md)

---

## Selection and input

### Color wells
- **What it is:** A color well lets people adjust the color of text, shapes, guides, and other onscreen elements.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - People need to choose or adjust a color, and tapping or clicking the well should open a color picker (system-provided or custom).
- **Don't use it when / use instead:**
  - You target tvOS or watchOS; color wells aren't supported.
  - You only need to pick from a fixed handful of options; a [Pop-up button](../references/components/menus-and-actions/pop-up-buttons.md) or [Segmented control](../references/components/selection-and-input/segmented-controls.md) may be simpler.
- **Rules:**
  - Consider the system-provided color picker for a familiar experience; it lets people save colors they can access from any app and stays consistent across iOS, iPadOS, and macOS.
  - After a selection, the color well updates to show the new color.
- **Platform notes:**
  - iOS, iPadOS, visionOS: No additional considerations. Not supported in tvOS or watchOS.
  - macOS: Clicking a color well highlights it to confirm it's active, then opens the color picker. Color wells support drag and drop between wells and from the picker.
- **Content/labels:** None given.
- **APIs:** `UIColorWell`, `UIColorPickerViewController` (UIKit); `NSColorWell` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<input type="color">` with a `<label>`, which opens the platform's native color picker; show the current swatch as the control's face.
- **Source:** [reference](../references/components/selection-and-input/color-wells.md)

### Combo boxes
- **What it is:** A combo box combines a text field with a pull-down button in a single control.
- **Platforms:** macos
- **Use it when:**
  - People should be able to enter a custom value or choose from a list of predefined values (custom values aren't added to the list).
  - You want to pair text input with a list of likely choices.
- **Don't use it when / use instead:**
  - Values must come only from the list; use a [Pop-up button](../references/components/menus-and-actions/pop-up-buttons.md).
  - You target any platform other than macOS; combine a [Text field](../references/components/selection-and-input/text-fields.md) with suggestions instead.
- **Rules:**
  - Populate the field with a meaningful default value from the list; it needn't be the first item.
  - Use an introductory label to let people know what types of items to expect.
  - Provide relevant choices; people value both custom entry and the most likely options.
  - Make sure list items aren't wider than the text field so they don't truncate.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Content/labels:** Introductory labels generally use title-style capitalization and end with a colon.
- **APIs:** `NSComboBox` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<input list="id">` with a `<datalist>`, or an `<input role="combobox" aria-expanded aria-controls aria-autocomplete="list">` paired with a `role="listbox"`; prefill a sensible default and size the list to the field's width.
- **Source:** [reference](../references/components/selection-and-input/combo-boxes.md)

### Digit entry views
- **What it is:** A digit entry view fills the entire screen and prompts people to enter a series of digits, like a PIN, using a digit-specific keyboard.
- **Platforms:** tvos
- **Use it when:**
  - A tvOS app needs a PIN or passcode, optionally with a title and prompt above the digits.
- **Don't use it when / use instead:**
  - You need general text entry on tvOS; use a [Text field](../references/components/selection-and-input/text-fields.md) with the linear keyboard.
  - You target any platform other than tvOS.
- **Rules:**
  - Use secure digit fields, which display asterisks instead of digits, whenever your app asks for sensitive data.
  - Clearly state the purpose of the digit entry view with a title and prompt.
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.
- **Content/labels:** Title and prompt explain why someone needs to enter digits.
- **APIs:** `TVDigitEntryViewController` (TVUIKit).
- **Web equivalent (translation, not Apple guidance):** A full-screen form of `<input type="password" inputmode="numeric" autocomplete="one-time-code" maxlength="1">` cells (or one masked field) with a heading and prompt text; mask the digits.
- **Source:** [reference](../references/components/selection-and-input/digit-entry-views.md)

### Image wells
- **What it is:** An image well is an editable version of an image view.
- **Platforms:** macos
- **Use it when:**
  - People should be able to copy, paste, drag in, or delete an image (for example a contact photo).
- **Don't use it when / use instead:**
  - The image is display-only; use an [Image view](../references/components/content/image-views.md).
  - The image should be clickable but not editable; use an image [button](../references/components/menus-and-actions/buttons.md).
- **Rules:**
  - Revert to a default image when necessary; if the well requires an image, redisplay the default when people clear it.
  - If your image well supports copy and paste, make sure the standard copy and paste menu items (and keyboard shortcuts) are available.
  - People can drag a new image into an image well without selecting it first.
- **Platform notes:**
  - Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Content/labels:** None given.
- **APIs:** `NSImageView` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A drop zone (`dragover`/`drop` handlers) wrapping an `<img>` preview and a hidden `<input type="file" accept="image/*">`, with paste support via the `paste` event and a Delete key or Remove button that restores the default image.
- **Source:** [reference](../references/components/selection-and-input/image-wells.md)

### Pickers
- **What it is:** A picker displays one or more scrollable lists of distinct values that people can choose from.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You're offering medium-to-long lists of items, or single or multipart values.
  - People need to choose a date, time, or both, including via a calendar view or numeric keypad.
- **Don't use it when / use instead:**
  - The list is fairly short; use a [Pull-down button](../references/components/menus-and-actions/pull-down-buttons.md), since a picker adds too much visual weight.
  - The set of items is very large; use a [List or table](../references/components/layout-and-organization/lists-and-tables.md), which can adjust in height and include an index.
- **Rules:**
  - Consider using a picker to offer medium-to-long lists of items.
  - Use predictable and logically ordered values (an alphabetized list of countries) because many values are hidden before interaction.
  - Avoid switching views to show a picker; display it in context below or near the field being edited, typically at the bottom of a window or in a popover.
  - Consider providing less granularity when specifying minutes in a date picker; the default minute list has 60 values (0 to 59), and you can use any interval that divides evenly into 60, such as quarter-hour intervals (0, 15, 30, 45).
  - The values shown, and their order, depend on the device language (and location for date pickers).
- **Platform notes:**
  - visionOS: No additional considerations.
  - iOS, iPadOS: Date picker styles: Compact (a button opening editable content in a modal view), Inline (wheels for time only; an inline calendar for dates and times), Wheels (scrolling wheels that also accept keyboard entry), Automatic. Modes: Date; Time (hours, minutes, optional AM/PM); Date and time; Countdown timer (hours and minutes up to 23 hours and 59 minutes, not available in inline or compact styles). Use a compact date picker when space is constrained; it shows the current value in the accent color and opens a modal calendar and time editor where people make multiple edits before tapping outside to confirm.
  - macOS: Choose a date picker style that suits your app: textual (limited space, specific selections) or graphical (browsing days in a calendar, selecting a range, or a clock face).
  - tvOS: Pickers are available with SwiftUI.
  - watchOS: People navigate pickers with the Digital Crown; the wheels style applies to lists and date and time pickers. You can configure a picker to display an outline, caption, and scrolling indicator. For longer lists, the navigation link style displays the picker as a button that opens the list; people can also scrub options with the Digital Crown without tapping.
- **Content/labels:** Captions and outlines are configurable on watchOS; order values predictably.
- **APIs:** `Picker`, `DatePicker`, `PickerStyle.navigationLink` (SwiftUI); `UIDatePicker`, `UIPickerView` (UIKit); `NSDatePicker` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<input type="date">`, `type="time"`, or `type="datetime-local"` with `step` for minute intervals (for example `step="900"` for 15 minutes); for value lists a `<select>` or an inline `role="listbox"` shown next to the field rather than on a new page.
- **Source:** [reference](../references/components/selection-and-input/pickers.md)

### Segmented controls
- **What it is:** A segmented control is a linear set of two or more segments, each of which functions as a button.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **Use it when:**
  - You're providing closely related choices that affect an object, state, or view (time ranges in Health; alignment or font attributes in Keynote).
  - It's important to group functions together or clearly show their selection state (single choice, or multiple choices on macOS).
  - You want a momentary set of actions without selection state (Mail's Reply, Reply All, Forward on macOS).
- **Don't use it when / use instead:**
  - You're switching between separate sections of an app; use a [Tab bar](../references/components/navigation-and-search/tab-bars.md).
  - You're switching views in the main window area on macOS; use a [Tab view](../references/components/layout-and-organization/tab-views.md) (a segmented control fits a toolbar or inspector).
  - You're filtering content on tvOS; consider a [Split view](../references/components/layout-and-organization/split-views.md).
  - You target watchOS; segmented controls aren't supported.
- **Rules:**
  - Use a segmented control to provide closely related choices that affect an object, state, or view.
  - Consider a segmented control when it's important to group functions together, or to clearly show their selection state.
  - Keep control types consistent within a single segmented control; don't mix action segments with selection-state segments.
  - Limit the number of segments in a control; aim for no more than about five to seven segments in a wide interface and no more than about five on iPhone.
  - In general, keep segment size consistent, including icon and title widths.
  - Prefer using either text or images, not a mix of both, in a single segmented control.
  - As much as possible, use content with a similar size in each segment.
  - Use nouns or noun phrases for segment labels; a text-labeled control doesn't need introductory text.
- **Platform notes:**
  - Not supported in watchOS.
  - iOS, iPadOS: Consider a segmented control to switch between closely related subviews (Calendar's New Event sheet switches between event and reminder); use a tab bar for separate sections.
  - macOS: Consider using introductory text to clarify the purpose of a segmented control, add labels below icon segments, and provide tooltips for each segment. Use a tab view in the main window area instead of a segmented control for view switching. Consider supporting spring loading (drag items over a segment and force click).
  - tvOS: Consider using a split view instead of a segmented control on screens that perform content filtering. Avoid putting other focusable elements close to segmented controls, because segments select on focus, not on click.
  - visionOS: Looking at an icon segment shows a tooltip with the descriptive text you supply.
- **Content/labels:** Nouns or noun phrases with title-style capitalization.
- **APIs:** `PickerStyle.segmented` (SwiftUI); `UISegmentedControl`, `isMomentary` (UIKit); `NSSegmentedControl`, `NSSegmentedControl.SwitchTracking.momentary` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A `role="radiogroup"` of equal-width toggle buttons (`role="radio"`, `aria-checked`) for single choice, `aria-pressed` buttons for multiple choice, or plain buttons for momentary actions; use either text or icons throughout, cap at five to seven segments, and support arrow-key movement.
- **Source:** [reference](../references/components/selection-and-input/segmented-controls.md)

### Sliders
- **What it is:** A slider is a horizontal track with a control, called a thumb, that people can adjust between a minimum and maximum value.
- **Platforms:** ios, ipados, macos, visionos, watchos
- **Use it when:**
  - People need to set a value within a finite range (brightness, opacity, image size) and benefit from direct manipulation.
  - Values repeat or continue indefinitely (rotation 0 to 360 degrees), where macOS offers a circular slider.
- **Don't use it when / use instead:**
  - You're adjusting audio volume on iOS or iPadOS; use a volume view, which includes a volume slider and an output device control.
  - People need exact values; supplement with a [Text field](../references/components/selection-and-input/text-fields.md) and a [Stepper](../references/components/selection-and-input/steppers.md).
  - You target tvOS; sliders aren't supported.
- **Rules:**
  - Customize a slider's appearance if it adds value (track color, thumb image and tint, left and right icons).
  - Use familiar slider directions: minimum on the leading side and maximum on the trailing side for horizontal sliders; minimum at the bottom and maximum at the top for vertical sliders.
  - Consider supplementing a slider with a corresponding text field and stepper, especially for wide ranges.
  - As the value changes, the track between the minimum and the thumb fills with color.
- **Platform notes:**
  - Not supported in tvOS.
  - iOS, iPadOS: Don't use a slider to adjust audio volume.
  - macOS: Sliders can include tick marks; linear thumbs are a narrow lozenge and circular thumbs a small circle with tick marks as dots. Consider giving live feedback as the value of a slider changes (Dock icon size). Choose a slider style that matches people's expectations: horizontal for fixed start and end points, circular for repeating or indefinite values (0 to 360 degrees, spins where four rotations equal 1440 degrees). Consider using a label to introduce a slider. Use tick marks to increase clarity and accuracy. Consider adding labels to tick marks for even greater clarity; labeling only the minimum and maximum is often sufficient, periodic labels help with nonlinear values, and a tooltip can show the thumb's value on hover.
  - visionOS: Prefer horizontal sliders; side-to-side gestures are easier than up and down.
  - watchOS: A slider appears as discrete steps or a continuous bar; people tap buttons on either side to change the value by a predefined amount. If necessary, create custom glyphs to communicate what the slider does; the defaults are plus and minus signs.
- **Content/labels:** macOS introductory labels use sentence-style capitalization and end with a colon.
- **APIs:** `Slider` (SwiftUI); `UISlider` (UIKit); `NSSlider` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<input type="range" min max step>` with a `<label>` and an `<output>` showing the value; fill the track up to the thumb with a gradient; pair with `<input type="number">` for wide ranges; optional `<datalist>` tick marks.
- **Source:** [reference](../references/components/selection-and-input/sliders.md)

### Steppers
- **What it is:** A stepper is a two-segment control that people use to increase or decrease an incremental value.
- **Platforms:** ios, ipados, macos, visionos
- **Use it when:**
  - People make small changes to a value with a few taps or clicks, next to a field that displays the current value.
- **Don't use it when / use instead:**
  - Values may vary widely; pair the stepper with a [Text field](../references/components/selection-and-input/text-fields.md) (for example number of copies when printing).
  - You need a continuous range; use a [Slider](../references/components/selection-and-input/sliders.md).
  - You target watchOS or tvOS; steppers aren't supported.
- **Rules:**
  - Make the value that a stepper affects obvious; the stepper itself doesn't display a value.
  - Consider pairing a stepper with a text field when large value changes are likely.
- **Platform notes:**
  - iOS, iPadOS, visionOS: No additional considerations. Not supported in watchOS or tvOS.
  - macOS: For large value ranges, consider supporting Shift-click to change the value quickly, for example by 10 times the default increment.
- **Content/labels:** None given.
- **APIs:** `UIStepper` (UIKit); `NSStepper` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<input type="number" step>` showing the value, flanked by decrement and increment `<button>`s with `aria-label`s and `aria-controls` pointing at the input; support Shift-click for a 10x step.
- **Source:** [reference](../references/components/selection-and-input/steppers.md)

### Text fields
- **What it is:** A text field is a rectangular area in which people enter or edit small, specific pieces of text.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You're requesting a small amount of information, such as a name or an email address.
  - You need sensitive input like a password (use a secure text field).
- **Don't use it when / use instead:**
  - People input larger amounts of text; use a [Text view](../references/components/content/text-views.md).
  - You need text input paired with a list of choices on macOS; use a [Combo box](../references/components/selection-and-input/combo-boxes.md).
  - On tvOS or watchOS, a list of options or buttons would gather the information more efficiently.
- **Rules:**
  - Use a text field to request a small amount of information, such as a name or an email address.
  - Show a hint in a text field to help communicate its purpose (placeholder like "Email" or "Password"), and consider a separate label because placeholders disappear when typing starts.
  - Use secure text fields to hide private data such as passwords.
  - To the extent possible, match the size of a text field to the quantity of anticipated text.
  - Evenly space multiple text fields; stack them vertically and use consistent widths (name fields one width, address and city another).
  - Ensure that tabbing between multiple fields flows as people expect.
  - Validate fields when it makes sense: an email address when people switch fields; a user name or password before they switch fields.
  - Use a number formatter to help with numeric data, and don't assume the presentation since formatting varies by locale.
  - Adjust line breaks according to the needs of the field: clip (default), wrap at character or word level, or truncate at the beginning, middle, or end.
  - Consider using an expansion tooltip to show the full version of clipped or truncated text.
  - In iOS, iPadOS, tvOS, and visionOS apps, show the appropriate keyboard type.
  - Minimize text entry in your tvOS and watchOS apps.
- **Platform notes:**
  - tvOS, visionOS: No additional considerations.
  - iOS, iPadOS: Display a Clear button in the trailing end of a text field to help people erase their input. Use images and buttons to provide clarity and functionality: the leading end indicates purpose, the trailing end offers features like bookmarking.
  - macOS: Consider using a combo box if you need to pair text input with a list of choices.
  - watchOS: Present a text field only when necessary; prefer a list of options.
- **Content/labels:** Placeholder text names the expected content ("Email", "Password"); a separate introductory label reminds people of the field's purpose.
- **APIs:** `TextField`, `SecureField` (SwiftUI); `UITextField` (UIKit); `NSTextField` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<input>` with a matching `type` (`email`, `password`, `tel`, `url`, `number`), `inputmode`, `autocomplete`, a visible `<label>`, and `placeholder` as a hint only; validate on blur for emails and on input for usernames and passwords; size with `width: Nch` to match expected length.
- **Source:** [reference](../references/components/selection-and-input/text-fields.md)

### Toggles
- **What it is:** A toggle lets people choose between a pair of opposing states, like on and off, using a different appearance to indicate each state.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - People choose between two opposing values that affect the state of content or a view (a switch in a list row, a checkbox, a toggle-style button).
  - On macOS you need checkboxes for hierarchies of settings or radio buttons for two to five mutually exclusive options.
- **Don't use it when / use instead:**
  - People need to choose from a list of items; use a [Pop-up button](../references/components/menus-and-actions/pop-up-buttons.md).
  - You need more than about five mutually exclusive options on macOS; use a pop-up button instead of radio buttons.
  - On iOS, the control sits outside a list row; use a button that behaves like a toggle, not a switch.
- **Rules:**
  - Use a toggle to help people choose between two opposing values that affect the state of content or a view.
  - Clearly identify the setting, view, or content the toggle affects; context usually suffices, macOS often adds a label, and toggle-style buttons use an icon with a changing background.
  - Make sure the visual differences in a toggle's state are obvious (fill, background shape, checkmark or dot); avoid relying solely on color.
- **Platform notes:**
  - tvOS, visionOS, watchOS: No additional considerations.
  - iOS, iPadOS: Use the switch toggle style only in a list row, with no label needed. Change the default color of a switch only if necessary; the default green works in most cases, and any custom color needs contrast with the off appearance. Outside of a list, use a button that behaves like a toggle, not a switch (Phone's filter button). Avoid supplying a label that explains the button's purpose; the icon and background states communicate it.
  - macOS: Use switches, checkboxes, and radio buttons in the window body, not the window frame (no toolbars or status bars). Switches: Prefer a switch for settings that you want to emphasize, such as turning a group of settings on or off. Within a grouped form, consider using a mini switch to control the setting in a single row (regular switch for the primary setting, mini for subordinate ones). In general, don't replace a checkbox with a switch. Checkboxes: a small square, empty when off, checkmark when on, dash when mixed, typically with a trailing title (no title in an editable checklist). Use a checkbox instead of a switch if you need to present a hierarchy of settings, using alignment and indentation. Consider using radio buttons if you need to present a set of more than two mutually exclusive options. Consider using a label to introduce a group of checkboxes if their relationship isn't clear, aligning its baseline with the first checkbox. Accurately reflect a checkbox's state in its appearance, including mixed state for a parent whose children differ. Radio buttons: small circles with labels in groups of two to five; selected is filled, deselected empty; the mixed state is rarely useful. Prefer a set of radio buttons to present mutually exclusive options; use checkboxes for multiple selections. Avoid listing too many radio buttons in a set; beyond about five options use a pop-up button. To present a single setting that can be on or off, prefer a checkbox; use a pair of labeled radio buttons only when a single checkbox is unclear. Use consistent spacing when you display radio buttons horizontally, measured from the longest label.
- **Content/labels:** Switches in iOS list rows need no label; macOS checkboxes carry a trailing title; group labels describe the set of options.
- **APIs:** `Toggle`, `ToggleStyle`, `ToggleStyle.switch`, `GroupedFormStyle`, `ControlSize` (SwiftUI); `UISwitch`, `UIButton.changesSelectionAsPrimaryAction` (UIKit); `NSButton.ButtonType.toggle`, `NSSwitch`, `NSButton.allowsMixedState` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<input type="checkbox">` with a `<label>` (styled as a switch via `role="switch"` and `aria-checked` when in a settings list), `indeterminate` for mixed state, `<input type="radio">` groups in a `<fieldset>` for two to five exclusive options, and `<button aria-pressed>` for icon toggles outside lists; never signal state with color alone.
- **Source:** [reference](../references/components/selection-and-input/toggles.md)

### Virtual keyboards
- **What it is:** On devices without physical keyboards, the system offers various types of virtual keyboards people can use to enter data.
- **Platforms:** ios, ipados, tvos, visionos, watchos
- **Use it when:**
  - A text field or text view becomes editable and you want keys optimized for the content (email, URL, numbers, phone, web search).
  - You need a custom input view for app-specific data entry (Numbers' numeric input view) or a systemwide custom keyboard extension (iOS, iPadOS, tvOS).
- **Don't use it when / use instead:**
  - You want a custom keyboard only inside your own app; create a custom input view, not a keyboard extension.
  - You'd duplicate system keyboard features (Emoji/Globe, Dictation) in a custom keyboard.
  - You need PIN entry on tvOS; use a [Digit entry view](../references/components/selection-and-input/digit-entry-views.md).
- **Rules:**
  - Choose a keyboard that matches the type of content people are editing; specifying a semantic content type lets the system pick and refine the keyboard. Types include ASCII capable, ASCII capable number pad, Decimal pad, Default, Email address, Name phone pad, Number pad, Numbers and punctuation, Phone pad, Twitter, URL, Web search.
  - Consider customizing the Return key type if it helps clarify the text-entry experience (a Search key when the field initiates search).
  - Make sure your custom input view makes sense in the context of your app, so people understand why the system keyboard is gone.
  - Play the standard keyboard sound while people type in a custom input view.
  - Provide an obvious and easy way to switch between keyboards in a custom keyboard, like the Globe key.
  - Avoid duplicating system-provided keyboard features; the Emoji/Globe and Dictation keys appear automatically on some devices.
  - Consider providing a keyboard tutorial in your app, not within the keyboard itself.
  - A virtual keyboard doesn't support keyboard shortcuts; custom keyboards can't be used in secure text fields or phone number fields.
- **Platform notes:**
  - Not supported in macOS.
  - iOS, iPadOS: Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface and keep important content and buttons visible. Place custom controls above the keyboard thoughtfully (input accessory view); keep them relevant, apply Liquid Glass if other views use it (a standard toolbar adopts it automatically), and use the layout guide and standard padding.
  - tvOS: A linear keyboard appears when people select a text field with the Siri Remote; a grid keyboard appears with other devices. A digit-specific keyboard appears for digit entry views.
  - visionOS: The system keyboard supports direct and indirect gestures and appears in a separate movable window; you don't need to account for its location in your layouts.
  - watchOS: A keyboard appears if the screen is large enough; otherwise people use dictation or Scribble. You can't change the keyboard type but can set the text content type to improve suggestions. People can also type on a nearby paired iPhone.
- **Content/labels:** Return key label matches the task (for example Search, Go).
- **APIs:** `keyboardType(_:)`, `textContentType(_:)`, `submitLabel(_:)`, `ToolbarItemPlacement` (SwiftUI); `UIKeyboardType`, `UITextContentType`, `UIReturnKeyType`, `inputViewController`, `inputAccessoryView`, `UIKeyboardLayoutGuide`, `playInputClick()` (UIKit).
- **Web equivalent (translation, not Apple guidance):** Set `type`, `inputmode` (`numeric`, `decimal`, `tel`, `email`, `url`, `search`), `enterkeyhint` (`search`, `go`, `done`), and `autocomplete` on inputs; use the `VirtualKeyboard` API or `env(keyboard-inset-height)` to keep fields and buttons above the keyboard.
- **Source:** [reference](../references/components/selection-and-input/virtual-keyboards.md)

---

## Status

### Activity rings
- **What it is:** Activity rings show an individual's daily progress toward Move, Exercise, and Stand goals.
- **Platforms:** ios, ipados, watchos
- **Use it when:**
  - Your app relates to health or fitness, especially if it contributes to HealthKit, and people expect to see their Activity progress (workout metrics screen, post-workout summary).
- **Don't use it when / use instead:**
  - You need to show any other kind of data, decoration, or branding; use a [Gauge](../references/components/status/gauges.md) or [Progress indicator](../references/components/status/progress-indicators.md) with a distinct style.
  - You need progress for more than one person.
  - You target macOS, tvOS, or visionOS; Activity rings aren't supported.
- **Rules:**
  - Display Activity rings when they're relevant to the purpose of your app.
  - Use Activity rings only to show Move, Exercise, and Stand information; never replicate or modify them, never show other data in them, and never show Move, Exercise, and Stand in another ring-like element.
  - Use Activity rings to show progress for a single person, making it obvious whose with a label, photo, or avatar.
  - Always keep the visual appearance of Activity rings the same: never change ring colors, filters, or opacity; always display on a black background; prefer enclosing rings and background in a circle by adjusting the enclosing view's corner radius rather than a mask; keep the black background visible around the outermost ring (add a thin black stroke if needed, no gradient or shadow); scale rings appropriately; design the surrounding interface to blend with the rings, never the reverse.
  - To display a label or value directly associated with a ring, use its matching RGB color: Move R-250, G-17, B-79; Exercise R-166, G-255, B-0; Stand R-0, G-255, B-246.
  - Maintain Activity ring margins: a minimum outer margin no less than the distance between rings, never cropped or encroached.
  - Differentiate other ring-like elements from Activity rings with padding, lines, labels, color, or scale.
  - Don't send notifications that repeat the same information the Activity app sends, and don't show an Activity ring element in notifications.
  - Don't use Activity rings for decoration (no labels or background graphics).
  - Don't use Activity rings for branding (no app icon or marketing).
- **Platform notes:**
  - iPadOS, watchOS: No additional considerations. Not supported in macOS, tvOS, or visionOS.
  - iOS: Available through `HKActivityRingView`. With an Apple Watch paired, iOS shows all three rings; without one, only the Move ring, approximating activity from steps and workouts from other apps. History may mix both styles.
  - watchOS: The element always contains three rings matching the Activity app.
- **Content/labels:** Ring labels are Move, Exercise, and Stand in their matching colors.
- **APIs:** `HKActivityRingView` (HealthKit).
- **Web equivalent (translation, not Apple guidance):** Only when rendering genuine HealthKit Move, Exercise, and Stand data: three concentric SVG arcs on a black circular background using the exact RGB values above, with an accessible text summary; otherwise use an ordinary ring gauge with different colors and styling.
- **Source:** [reference](../references/components/status/activity-rings.md)

### Gauges
- **What it is:** A gauge displays a specific numerical value within a range of values.
- **Platforms:** ios, ipados, macos, visionos, watchos
- **Use it when:**
  - You're showing where a current value sits in a known range (temperature, battery), optionally with endpoint labels and a color spectrum.
  - You want an accessory-style gauge that echoes watchOS complications in iOS Lock Screen widgets.
- **Don't use it when / use instead:**
  - You're showing the progress of an operation; use a [Progress indicator](../references/components/status/progress-indicators.md).
  - You're showing a ranking on macOS; use a [Rating indicator](../references/components/status/rating-indicators.md).
  - You target tvOS; gauges aren't supported.
- **Rules:**
  - Write succinct labels that describe the current value and both endpoints of the range; VoiceOver reads the visible labels.
  - Consider filling the path with a gradient to help communicate the purpose of the gauge (red to blue for hot to cold).
  - Anatomy: a circular or linear path; the standard style shows an indicator at the value, the capacity style fills up to the value; the accessory variant resembles complications.
- **Platform notes:**
  - iOS, iPadOS, visionOS, watchOS: No additional considerations. Not supported in tvOS.
  - macOS: Also defines a level indicator for capacity, rating, or rarely relevance. Capacity can be Continuous (a translucent track filling with a solid bar) or Discrete (equally sized segments that fill completely, never partially). Consider using the continuous style for large ranges. Consider changing the fill color to inform people about significant parts of the range; the default fill is green, and the tiered state shows several colors in one indicator. The relevance style shades a horizontal bar, for example in search results.
- **Content/labels:** Labels for current value and both endpoints.
- **APIs:** `Gauge` (SwiftUI); `NSLevelIndicator` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<meter min max low high optimum value>` for a value in a range (styled as a bar or circular SVG), with a visible label and endpoint labels; use `<progress>` only for operations.
- **Source:** [reference](../references/components/status/gauges.md)

### Progress indicators
- **What it is:** Progress indicators let people know that your app isn't stalled while it loads content or performs lengthy operations.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - A task has a well-defined duration (file conversion): use a determinate progress bar or circular indicator.
  - A task is unquantifiable (loading or syncing complex data): use an indeterminate activity indicator (spinner; macOS also has an indeterminate bar).
  - People should be able to reload a table immediately on iOS or iPadOS: use a refresh control.
- **Don't use it when / use instead:**
  - You're displaying a static value within a range; use a [Gauge](../references/components/status/gauges.md).
  - You could show a determinate indicator; indeterminate ones don't help people estimate time.
- **Rules:**
  - When possible, use a determinate progress indicator.
  - Be as accurate as possible when reporting advancement; even out the pace rather than showing 90 percent in five seconds and the last 10 percent in 5 minutes.
  - Keep progress indicators moving so people know something is continuing to happen; if a process stalls, explain the problem and what people can do.
  - When possible, switch a progress bar from indeterminate to determinate once the duration is known.
  - Don't switch from the circular style to the bar style.
  - If it's helpful, display a description that provides additional context; avoid vague terms like loading or authenticating.
  - Display a progress indicator in a consistent location.
  - When it's feasible, let people halt processing with a Cancel button, adding Pause if interruption has side effects.
  - Let people know when halting a process has a negative consequence, with an [alert](../references/components/presentation/alerts.md) to confirm or resume.
  - All progress indicators are transient, appearing only while an operation is ongoing.
- **Platform notes:**
  - tvOS, visionOS: No additional considerations.
  - iOS, iPadOS: Refresh content controls are hidden activity indicators revealed by dragging down a view (Mail's Inbox). Perform automatic content updates; don't make people initiate every refresh. Supply a short title only if it adds value (Podcasts shows the last update time), never to explain how to refresh.
  - macOS: Indeterminate indicators can be a bar or circular. Prefer an activity indicator (spinner) to communicate the status of a background operation or when space is constrained (inside a text field or next to a button). Avoid labeling a spinning progress indicator.
  - watchOS: Indicators are white over the scene background by default; change the color via tint.
- **Content/labels:** Descriptions are accurate and succinct; avoid loading and authenticating.
- **APIs:** `ProgressView` (SwiftUI); `UIProgressView`, `UIActivityIndicatorView`, `UIRefreshControl` (UIKit); `NSProgressIndicator` (AppKit).
- **Web equivalent (translation, not Apple guidance):** `<progress value max>` for determinate, `<progress>` without `value` or a `role="status"` spinner with `aria-busy` for indeterminate; announce changes through `aria-live="polite"`; add Cancel and Pause buttons when safe; keep the same shape for the whole operation.
- **Source:** [reference](../references/components/status/progress-indicators.md)

### Rating indicators
- **What it is:** A rating indicator uses a series of horizontally arranged graphical symbols, by default stars, to communicate a ranking level.
- **Platforms:** macos
- **Use it when:**
  - You're showing or letting people set a ranking level for items in a macOS app (rounded to whole symbols).
- **Don't use it when / use instead:**
  - You need to show a value within a range rather than a rank; use a [Gauge](../references/components/status/gauges.md).
  - You target any platform other than macOS; build a custom accessible rating control.
- **Rules:**
  - Make it easy to change rankings; let people adjust the rank of individual items inline without navigating to a separate editing screen.
  - If you replace the star with a custom symbol, make sure that its purpose is clear.
  - The indicator doesn't display partial symbols; it rounds to complete symbols, and symbols keep a constant distance apart regardless of width.
- **Platform notes:**
  - macOS: No additional considerations. Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Content/labels:** Stars by default.
- **APIs:** `NSLevelIndicator.Style.rating` (AppKit).
- **Web equivalent (translation, not Apple guidance):** A `role="radiogroup"` of star `<input type="radio">` controls labeled "1 star" through "5 stars" for editing inline, or a read-only row of star icons with an `aria-label` like "4 of 5 stars"; whole stars only.
- **Source:** [reference](../references/components/status/rating-indicators.md)

---

## System experiences

### App Shortcuts
- **What it is:** An App Shortcut gives people access to your app's key functions or content throughout the system.
- **Platforms:** ios, ipados, visionos, watchos
- **Use it when:**
  - You want key tasks available through Siri, Spotlight, the Shortcuts app, the Action button, or an Apple Pencil squeeze, immediately after installation.
  - You're exposing unique features or custom content in areas that app schemas don't cover.
- **Don't use it when / use instead:**
  - Your app is in a common domain; consider adopting app schemas so Siri and Apple Intelligence surface features contextually.
  - You need more than 10 App Shortcuts; each app can include up to 10.
  - You're on macOS; App Shortcuts aren't supported, but App Intents actions work in the Shortcuts app.
- **Rules:**
  - To surface common types of app functionality throughout the system, consider adopting app schemas instead.
  - Offer App Shortcuts for your app's most common and important tasks, preferably ones people complete without leaving their context.
  - Add flexibility by letting people choose from a set of options with a single optional parameter ("Start [morning, daily, sleep] meditation"), using predictable, familiar values.
  - Ask for clarification in response to a request that's missing optional information; suggest a likely default and a short list of alternatives.
  - Keep voice interactions simple; if a phrase feels complicated aloud it's too hard to remember, so ask for extra information in a subsequent step.
  - Make App Shortcuts discoverable in your app with occasional tips when people perform common actions.
  - Respond with [Snippets](../references/components/system-experiences/snippets.md) for static information or dialog options and [Live Activities](../references/components/system-experiences/live-activities.md) for information that changes over time.
  - Provide enough detail for interaction on audio-only devices like AirPods and HomePod by including all critical information in the full dialogue text.
  - Provide brief, memorable activation phrases and natural variants; you must include your app name but can be creative (Keynote: "Create a Keynote", "Add a new presentation in Keynote").
- **Platform notes:**
  - visionOS, watchOS: No additional considerations. Not supported in tvOS.
  - iOS, iPadOS: App Shortcuts appear in Spotlight's Top Hit area or the Shortcuts area, each with an SF Symbol or a preview image of the linked item. Order shortcuts based on importance; the system later prioritizes the ones people use most.
  - macOS: App Shortcuts aren't supported; App Intents actions can be used in custom shortcuts on Mac.
- **Content/labels:** When referring to App Shortcuts or the Shortcuts app, always use title case and make sure Shortcuts is plural. When referring to individual shortcuts, use lowercase ("Run a shortcut by asking Siri").
- **APIs:** App Intents, App Shortcuts, `AppShortcutPhrase`, `SiriTipUIView`, `LiveActivityIntent`, `IntentDialog.init(full:supporting:systemImageName:)`, app schema domains (App Intents); SiriKit.
- **Web equivalent (translation, not Apple guidance):** Expose the same key tasks as deep-linkable URLs declared in the web app manifest `shortcuts` and as structured data or Open Graph actions; keep names short and verb-led and offer at most a handful.
- **Source:** [reference](../references/components/system-experiences/app-shortcuts.md)

### Complications
- **What it is:** A complication displays timely, relevant information on the watch face, where people can view it each time they raise their wrist.
- **Platforms:** watchos
- **Use it when:**
  - You have essential, dynamic content people want at a glance and want quick launching into a relevant area of your watchOS app.
  - You want to appear on more watch faces by supporting multiple complication families (circular, corner, inline, rectangular) and the legacy templates.
- **Don't use it when / use instead:**
  - The content is static and not meaningful; a static complication tends to lose its prominent position.
  - You need glanceable content on iPhone, iPad, Mac, or Vision Pro; use [Widgets](../references/components/system-experiences/widgets.md) (Lock Screen widgets follow complication principles).
- **Rules:**
  - Identify essential, dynamic content that people want to view at a glance.
  - Support all complication families when possible; if a family can't show useful data, provide an image like your app icon so people can still launch the app.
  - Consider creating multiple complications for each family, and showcase them in a shareable [watch face](../references/components/system-experiences/watch-faces.md).
  - Define a different deep link for each complication you support.
  - Keep privacy in mind; the Always-On display can be visible to others.
  - Carefully consider when to update data; timeline entries are limited per day and per app, so pick times that enhance usefulness.
  - Choose a ring or gauge style based on the data you need to display: closed for a percentage of a whole (battery), open for arbitrary min and max (speed), segmented for rapid value changes within an app-defined range (Noise).
  - Make sure images look good in tinted mode: avoid color as the only way to communicate information, and provide a tinted-mode version of a full-color image when needed.
  - Recognize that people might prefer to use tinted mode for complications; the system desaturates and tints with the wearer's color.
  - When creating complication content, generally use line widths of two points or greater.
  - Provide a set of static placeholder images for each complication you support; sizes may differ from actual images.
  - Rectangular layouts may appear in the Smart Stack starting with watchOS 10; optimize with meaningful background color or content, intents that specify relevancy, and a custom Smart Stack layout.
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, tvOS, or visionOS.
  - Circular (Infograph, Infograph Modular, X-Large): regular image sizes 42x42 pt (40mm), 44.5x44.5 pt (41mm), 47x47 pt (44mm), 50x50 pt (45mm/49mm); closed gauge 27, 28.5, 31, 32 pt square; open gauge 11, 11.5, 12, 13 pt square; stack 28x14, 29.5x15, 31x16, 33.5x16.5 pt; the system applies a circular mask; bezel text can fill nearly 180 degrees. Default text: Rounded, Medium, 12 pt (40mm), 12.5 pt (41mm), 13 pt (44mm), 14.5 pt (45mm/49mm). Extra-large circular: image 120, 127, 132, 143 pt square; open gauge 31, 33, 33, 37 pt; closed gauge 77, 81.5, 87, 91.5 pt; stack 80x40, 85x42, 87x44, 95x48 pt; text Rounded, Medium, 34.5, 36.5, 36.5, 41 pt. Placeholders: circular and bezel 42, 44.5, 47, 50 pt square; extra large 120, 127, 132, 143 pt square.
  - Corner (Infograph): circular image 32, 34, 36, 38 pt square; gauge and text images 20, 21, 22, 24 pt square; circular mask applied; placeholders 20, 21, 22, 24 pt square; text Rounded, Semibold, 10 pt (40mm), 10.5 pt (41mm), 11 pt (44mm), 12 pt (45mm/49mm).
  - Inline: utilitarian small (corner rectangles on Chronograph, Simple) with flat images 9-21x9 pt (38mm), 10-22x10 pt (40mm/42mm), 10.5-23.5x21 pt (41mm), N/A (44mm), 12-26x12 pt (45mm/49mm); ring 14, 14, 15, 16, 16.5 pt square; square 20, 22, 23.5, 25, 26 pt square. Utilitarian large spans the bottom (Utility, Motion) and is text-based with an optional leading icon using the same flat sizes.
  - Rectangular: large image with title 150x47 pt (40mm), 159x50 pt (41mm), 171x54 pt (44mm), 178.5x56 pt (45mm/49mm); large image without title 162x69, 171.5x73, 184x78, 193x82 pt; standard body and text gauge images 12, 12.5, 13.5, 14.5 pt square; large-image layouts include a four-point corner radius; text Rounded, Medium, 16.5, 17.5, 18, 19.5 pt.
  - Legacy templates: Circular small (ring 20, 22, 23.5, 24, 26 pt; simple 16, 18, 19, 20, 21.5 pt; stack 16x7, 17x8, 18x8.5, 19x9, 19x9.5 pt; placeholder matches simple), Modular small (ring 18, 19, 20, 21, 22.5 pt; simple 26, 29, 30.5, 32, 34.5 pt; stack 26x14, 29x15, 30.5x16, 32x17, 34.5x18 pt), Modular large (columns, standard body, table images 11-32x11, 12-37x12, 12.5-39x12.5, 14-42x14, 14.5-44x14.5 pt), Extra large (ring 63, 66.5, 70.5, 73, 79 pt; simple 91, 101.5, 107.5, 112, 121 pt; stack 78x42, 87x45, 92x47.5, 96x51, 103.5x53.5 pt), all for 38mm, 40mm/42mm, 41mm, 44mm, 45mm/49mm respectively; stack widths are maximums.
- **Content/labels:** Prefer WidgetKit for watchOS 9 and later; legacy templates don't take on the wearer's selected color.
- **APIs:** WidgetKit, `WidgetRenderingMode`, `TimelineProvider.placeholder(in:)`, `WidgetFamily.accessoryRectangular` (WidgetKit); `CLKComplicationDataSource` (ClockKit, for earlier watchOS).
- **Web equivalent (translation, not Apple guidance):** No direct equivalent; the closest analog is a tiny, frequently refreshed summary tile (for example a badge via the Badging API or a compact widget in a dashboard) that deep-links to the relevant screen and remains legible in a single tint color with 2px minimum strokes.
- **Source:** [reference](../references/components/system-experiences/complications.md)

### Controls
- **What it is:** A control provides quick access to a feature of your app from Control Center, the Lock Screen, or the Action button.
- **Platforms:** ios, ipados, macos
- **Use it when:**
  - An action or two-state toggle provides real benefit without launching the app (start a Live Activity, toggle a light, launch a camera experience on a locked device).
- **Don't use it when / use instead:**
  - The control would merely open your app; offer real functionality or a deep link to a specific area.
  - You need glanceable information rather than an action; use [Widgets](../references/components/system-experiences/widgets.md).
  - You target watchOS, tvOS, or visionOS; controls aren't supported.
- **Rules:**
  - Offer controls for actions that provide the most benefit without having to launch your app.
  - Update controls when someone interacts with them, when an action completes, or remotely with a push notification, so they reflect state and progress.
  - Choose a descriptive symbol that suggests the behavior of the control; for toggles provide symbols for both on and off states (`door.garage.open`, `door.garage.closed`).
  - Use symbol animations to highlight state changes; animate toggles between states and animate buttons indefinitely while an action with a duration performs.
  - Select a tint color that works with your app's brand; the system applies it to a toggle's on-state symbol and in the Dynamic Island.
  - Help people provide additional information the system needs to perform an action by prompting for configuration when they first add the control.
  - Provide hint text for the Action button, constructed with verbs ("Hold for Silent").
  - If your control title or value can vary, include a placeholder for the controls gallery and Action button assignment.
  - Hide sensitive information when the device is locked by letting the system redact the title and value, and optionally the symbol state (shown as off).
  - Require authentication for actions that affect security (unlocking a door, starting a car).
  - Camera experiences on a locked device (iOS 18 and later): use the same camera UI in your app and your camera experience; provide instructions for adding the control; any task beyond capture requires unlocking.
- **Platform notes:**
  - iOS, iPadOS, macOS: No additional considerations. Not supported in watchOS, tvOS, or visionOS.
  - Anatomy: a symbol, a title, and an optional value. Control Center shows the symbol and, at larger sizes, title and value; the Lock Screen shows the symbol; the Action button shows the symbol and value in the Dynamic Island.
- **Content/labels:** Title describes what the control relates to (the name of a light); value shows state (on or off); hint text uses verbs.
- **APIs:** `ControlWidgetConfiguration.promptsForUserConfiguration()`, `controlWidgetActionHint(_:)` (SwiftUI); `SymbolEffect` (Symbols); `IntentAuthenticationPolicy` (App Intents); LockedCameraCapture; WidgetKit.
- **Web equivalent (translation, not Apple guidance):** A compact icon `<button>` or `role="switch"` in a persistent quick-actions bar or PWA shortcut, with an `aria-label` combining title and value, animated icon state changes, and re-authentication before security-sensitive actions.
- **Source:** [reference](../references/components/system-experiences/controls.md)

### Live Activities
- **What it is:** A Live Activity lets people track the progress of an activity, event, or task at a glance.
- **Platforms:** ios, ipados, macos, watchos
- **Use it when:**
  - A task or event has a defined beginning and end and lasts a short to medium duration (not exceeding eight hours), with frequent content and status updates (delivery ETA, live score, workout metrics).
  - People benefit from glanceable updates in the Dynamic Island, Lock Screen, StandBy, Mac menu bar, Apple Watch Smart Stack, or CarPlay Dashboard.
- **Don't use it when / use instead:**
  - You want to display ads or promotions.
  - The information isn't time-bound or doesn't change; use [Widgets](../references/components/system-experiences/widgets.md).
  - You'd send repeated push [Notifications](../references/components/system-experiences/notifications.md) for the same updates; don't do both.
- **Rules:**
  - Offer Live Activities for tasks and events that have a defined beginning and end, not exceeding eight hours.
  - Focus on important information that people need to see at a glance; tapping opens the app for details.
  - Don't use a Live Activity to display ads or promotions.
  - Avoid displaying sensitive information; show an innocuous summary or redact views.
  - Create a Live Activity that matches your app's visual aesthetic and personality in both dark and light appearances.
  - If you include a logo mark, display it without a container; don't use the entire app icon.
  - Don't add elements to your app that draw attention to the Dynamic Island.
  - Ensure text is easy to read: large, heavier-weight text (medium weight or higher); use small text sparingly.
  - Support compact, minimal, expanded, and Lock Screen presentations; adapt to different screen sizes and presentations using the specifications.
  - Adjust element size and placement for efficient use of space.
  - Support limited width presentations: fit compact and minimal presentations inside a 28pt-diameter circle (Dynamic Island in landscape) using abbreviations or graphics; if both sides can't make sense, adopt a leading view only.
  - Use familiar layouts for custom views with the Apple Design Resources templates.
  - Use consistent margins and concentric placement; use `ContainerRelativeShape` for rounded elements near corners instead of hard-coded radii.
  - When separating a block of content, place it in an inset container shape or use a thick line; don't draw to the edge of the Dynamic Island.
  - Dynamically change the height of your Live Activity on the Lock Screen or in the expanded presentation as the amount of information changes.
  - Carefully consider using a custom background color and opacity; only the Lock Screen presentation supports it, and contrast matters on Always-On displays.
  - Use color to express the character and identity of your app; the Dynamic Island background is opaque black, so bold colors help.
  - Tint your Live Activity's key line color so that it matches your content.
  - Use animations (system or custom, maximum duration two seconds) to reinforce information and bring attention to updates; none play on Always-On displays with reduced luminance.
  - Animate layout changes, preserving existing elements by moving them rather than removing and re-adding.
  - Try to avoid overlapping elements during transitions.
  - Make sure tapping the Live Activity opens your app at the right location.
  - Focus on simple, direct actions; limit interactivity to essential functionality, preferably a single element.
  - Consider letting people respond to event or progress updates (a button to contact the driver).
  - Start Live Activities at appropriate times, and make it easy for people to turn them off in your app.
  - Offer an App Shortcut that starts your Live Activity.
  - Update a Live Activity only when new content is available.
  - Alert people only for essential updates that require their attention, and don't use push notifications alongside Live Activities for the same updates.
  - Let people track multiple events efficiently with a single Live Activity that rotates through events.
  - Always end a Live Activity immediately when the task or event ends, and consider setting a custom dismissal time; it stays up to four hours on the Lock Screen, Mac menu bar, and Smart Stack, and 15 to 30 minutes is adequate in most cases.
  - Start with the iPhone design, then refine it for other contexts (StandBy, CarPlay, Apple Watch).
  - Compact: Focus on the most important information. Ensure unified information and design of the leading and trailing elements. Keep content as narrow as possible and ensure it's snug against the TrueDepth camera with balanced leading and trailing views. Link to relevant app content, with both elements opening the same screen.
  - Minimal: Ensure that your Live Activity is recognizable; show updated information rather than just a logo (Timer shows remaining time).
  - Expanded: Maintain the relative placement of elements between presentations. Wrap content tightly around the TrueDepth camera.
  - Lock Screen: Don't replicate notification layouts. Choose colors that work well on a personalized Lock Screen, using custom backgrounds and tints sparingly. Make sure your design, assets, and colors look great and offer enough contrast in Dark Mode and on an Always-On display. Verify the generated color of the dismiss button. Use standard margins to align your design with notifications; the standard layout margin is 14 points.
  - StandBy: Update your layout for StandBy (scaled 2x). Consider using the default background color in StandBy. Use standard margins and avoid extending graphic elements to the edge of the screen. Verify your design in Night Mode (red tint).
  - CarPlay: Consider creating a custom layout if your Live Activity would benefit from larger text or additional information (`ActivityFamily.small`). Carefully consider including buttons or toggles in your custom layout; the system deactivates interactive elements in CarPlay.
- **Platform notes:**
  - iOS, iPadOS: No additional considerations. Not supported in tvOS or visionOS.
  - macOS: Active Live Activities appear in the menu bar of a paired Mac using compact, minimal, and expanded presentations; clicking launches iPhone Mirroring. Use the iOS dimensions.
  - watchOS: Appears at the top of the Smart Stack combining the compact leading and trailing elements; tapping opens your watchOS app or a full-screen view with a button to open the iPhone app. Consider creating a custom watchOS layout for more information or a button or toggle. Carefully consider including buttons or toggles in your custom layout, because it also applies in CarPlay. Focus on essential information and significant updates (progress, interactive controls, score changes).
  - Specifications: CarPlay sizes 240x78, 240x100, 170x78 pt, tested at Widescreen 1920x720, Portrait 900x1200, Standard 800x480. iOS (portrait screen 430x932): compact 62.33x36.67, minimal 36.67 to 45 wide x 36.67, expanded 408x84 to 160, Lock Screen 408x84 to 160, limited width 28x28; (393x852): compact 52.33x36.67, minimal 36.67 to 45 x 36.67, expanded and Lock Screen 371x84 to 160, limited width 28x28. iPadOS Lock Screen: 500x84 to 160 (1366x1024); 425x84 to 160 (1194x834, 1012x834, 1080x810, 1024x768). watchOS Smart Stack: 152x69.5 (40mm), 165x72.5 (41mm), 176x72.5 (42mm), 173x76.5 (44mm), 184x80.5 (45mm), 194x80.5 (46mm), 198x81.5 (49mm Ultra 3, 4), 191x81.5 (49mm Ultra 1, 2).
- **Content/labels:** Prioritize essential, glanceable information; shortened units or less precise data keep the compact layout balanced.
- **APIs:** ActivityKit, `ActivityFamily.small`, `ContainerRelativeShape`, `activitySystemActionForegroundColor(_:)`, `padding(_:_:)`, `isDynamicIslandLimitedInWidth` (SwiftUI, WidgetKit); `LiveActivityIntent` (App Intents).
- **Web equivalent (translation, not Apple guidance):** A persistent, periodically updated status region (`role="status"`, `aria-live="polite"`) pinned to the viewport, backed by push notifications or Background Sync for updates, with large bold text, at most one action button, and automatic removal shortly after the event ends.
- **Source:** [reference](../references/components/system-experiences/live-activities.md)

### Notifications
- **What it is:** A notification gives people timely, high-value information they can understand at a glance.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **Use it when:**
  - You have timely, valuable information people want when they're not in your app, and they have granted consent.
  - People can perform simple tasks from the notification with up to four action buttons.
- **Don't use it when / use instead:**
  - You need to display an error message; use an [Alert](../references/components/presentation/alerts.md).
  - Your app is in the foreground; present the information in the view instead (increment a badge, insert data subtly).
  - You're tracking an ongoing event with frequent updates; use a [Live Activity](../references/components/system-experiences/live-activities.md) and don't double up.
- **Rules:**
  - Provide concise, informative notifications.
  - Avoid sending multiple notifications for the same thing, even if someone hasn't responded.
  - Avoid sending a notification that tells people to perform specific tasks within your app; offer notification actions instead.
  - Use an alert, not a notification, to display an error message.
  - Handle notifications gracefully when your app is in the foreground.
  - Avoid including sensitive, personal, or confidential information in a notification.
  - Create a short title if it provides context (headline, event name, email subject); if only a generic title like New Document is possible, let the system display your app name instead.
  - Write succinct, easy-to-read notification content; don't truncate, the system does.
  - Provide generically descriptive text to display when notification previews aren't available ("Friend request", "New comment", "Reminder", "Shipment").
  - Avoid including your app name or icon; the system shows a large app icon automatically (or the sender's avatar badged with your icon in communication notifications).
  - Consider providing a sound to supplement your notifications: short, distinctive, professionally produced, never relied on for important information; vibration can't be set programmatically.
  - Provide beneficial actions that make sense in the context of your notification, up to four buttons for common, time-saving tasks.
  - Avoid providing an action that merely opens your app.
  - Prefer nondestructive actions; give enough context for any destructive one.
  - Provide a simple, recognizable interface icon for each notification action, shown on the trailing side of the action title.
  - Use a badge only to show people how many unread notifications they have; never for weather, dates, stock prices, or scores.
  - Make sure badging isn't the only method you use to communicate essential information.
  - Keep badges up to date; reducing the count to zero removes related notifications from Notification Center.
  - Avoid creating a custom image or component that mimics the appearance or behavior of a badge.
- **Platform notes:**
  - iOS, iPadOS, macOS, tvOS, visionOS: No additional considerations.
  - watchOS: Notifications have a short look (appears on wrist raise, disappears on lower) and a long look (detailed, scrollable, dismissed by tap or lowering the wrist). Avoid using a short look as the only way to communicate important information. Keep privacy in mind in short looks; avoid sensitive information in the title. Consider using a rich, custom long-look notification with SwiftUI animations, SpriteKit, or SceneKit. At the minimum, provide a static interface; prefer providing a dynamic interface too, packaging static resources with the app. Choose a background appearance for the sash (custom color or blurred over a photo). Choose a background color for the content area; the default is transparent, and white with 18% opacity matches system notifications. Provide up to four custom actions below the content area; the system always adds a Dismiss button at the bottom. Keep double tap in mind when choosing the order of custom actions, since double tap runs the first nondestructive action; list the most common choice first.
- **Content/labels:** Title: title-style capitalization, no ending punctuation. Body: complete sentences, sentence case, proper punctuation. Hidden-preview placeholder: sentence-style capitalization. Action buttons: short title-case term or phrase describing the result, no app name, brief to avoid truncation, localized.
- **APIs:** `UNNotificationCategory.hiddenPreviewsBodyPlaceholder`, `UNNotificationSound`, Asking permission to use notifications, Handling notifications and notification-related actions (User Notifications); User Notifications UI; Animations (SwiftUI); SpriteKit; SceneKit.
- **Web equivalent (translation, not Apple guidance):** The Notifications API via a service worker (`showNotification` with `title`, `body`, up to a few `actions` with icons, `tag` to collapse duplicates, `silent` or a short sound), only after permission granted by a user gesture; use the Badging API solely for unread counts; never use a notification for in-page errors.
- **Source:** [reference](../references/components/system-experiences/notifications.md)

### Snippets
- **What it is:** When someone performs a task with Siri or an App Shortcut, a snippet shows the result or asks for confirmation.
- **Platforms:** ios, ipados, macos
- **Use it when:**
  - An app intent needs to confirm or cancel an action (a confirmation snippet, optionally with options) or show information that needs no further action (a result snippet).
  - You're responding to Siri, Spotlight, or the Shortcuts app with a compact custom view (weather forecast, daily goal progress, order confirmation).
- **Don't use it when / use instead:**
  - The information keeps changing over time; use a [Live Activity](../references/components/system-experiences/live-activities.md).
  - You need to show a lot of detail; deep-link to the content in your app instead.
  - You target tvOS, visionOS, or watchOS; snippets aren't supported.
- **Rules:**
  - Ensure legibility with sufficient contrast against the system background in light and dark appearances and consistent margins.
  - Keep content concise; custom views are no taller than the 400-point maximum height, and fonts scale with people's preferred text size.
  - Choose a descriptive label for a confirmation snippet's primary button (Order rather than OK or Proceed); the system default is Continue.
  - Communicate a snippet's purpose visually; prefer omitting the spoken dialogue text from the visual representation and let the custom view convey the information.
  - Anatomy: dialogue (spoken by Siri, shown above the view by default), custom view (may include buttons), and system-provided buttons (confirmation: secondary Cancel plus a primary button with a customizable label; result: a single Done button).
- **Platform notes:**
  - iOS, iPadOS, macOS: No additional considerations. Not supported in tvOS, visionOS, or watchOS.
- **Content/labels:** Primary button label from the system-provided set or a custom verb; Cancel and Done are system provided.
- **APIs:** App Intents, Displaying static and interactive snippets, `ConfirmationActionName` (App Intents).
- **Web equivalent (translation, not Apple guidance):** A compact `<dialog>` card (max height about 400px) with a visual summary, an optional Cancel plus a verb-labeled primary button for confirmations, or a single Done button for results; don't repeat the summary text as both heading and body.
- **Source:** [reference](../references/components/system-experiences/snippets.md)

### Status bars
- **What it is:** A status bar appears along the upper edge of the screen and displays information about the device's current state, like the time, cellular carrier, and battery level.
- **Platforms:** ios, ipados
- **Use it when:**
  - Your iOS or iPadOS app's layout touches the top edge and you must keep the status bar readable over your content.
  - You're showing full-screen media and want to hide the status bar temporarily.
- **Don't use it when / use instead:**
  - You want to hide the status bar permanently; people would have to leave your app to check the time or Wi-Fi.
  - You target macOS, tvOS, visionOS, or watchOS; status bars aren't supported.
- **Rules:**
  - Obscure content under the status bar; its background is transparent by default, so keep it readable and don't imply that content behind it is interactive; prefer a scroll edge effect to place a blurred view behind it.
  - Consider temporarily hiding the status bar when displaying full-screen media (Photos does this when browsing full-screen photos).
  - Avoid permanently hiding the status bar; let people redisplay it with a simple, discoverable gesture such as a single tap.
- **Platform notes:**
  - iOS, iPadOS: No additional considerations. Not supported in macOS, tvOS, visionOS, or watchOS.
- **Content/labels:** None given.
- **APIs:** `ScrollEdgeEffectStyle` (SwiftUI); `UIScrollEdgeEffect`, `UIStatusBarStyle`, `preferredStatusBarStyle` (UIKit).
- **Web equivalent (translation, not Apple guidance):** Respect `env(safe-area-inset-top)` with `viewport-fit=cover`, set `<meta name="theme-color">` so the browser's status area stays legible, keep a blurred or solid backdrop under the top inset, and use the Fullscreen API only for media with an easy exit.
- **Source:** [reference](../references/components/system-experiences/status-bars.md)

### Top Shelf
- **What it is:** The Apple TV Home Screen provides an area called Top Shelf, which showcases your content in a rich, engaging way while also giving people access to their favorite apps in the Dock.
- **Platforms:** tvos
- **Use it when:**
  - You want to highlight new, featured, or recommended content and let people jump directly into playback or details when your app is in the Dock and focused.
  - You can supply dynamic full-screen content (carousel actions, carousel details, sectioned content row, scrolling inset banner).
- **Don't use it when / use instead:**
  - You want to show advertisements or prices.
  - You want a static image to look interactive; static Top Shelf images aren't focusable.
  - You target any platform other than tvOS.
- **Rules:**
  - Help people jump right into your content; carousel actions and carousel details include a primary playback button and a More Info button by default.
  - Feature new content (new releases, episodes, upcoming shows) and avoid promoting content people already purchased, rented, or watched.
  - Personalize people's favorite content with targeted recommendations, resume playback, or jump back into gameplay.
  - Avoid showing advertisements or prices; show prices only when people show interest.
  - Showcase compelling dynamic content, preferring layered images.
  - If you don't provide the recommended full-screen content, supply at least one static image as a fallback at 2320x720 pt (2320x720 px @1x, 4640x1440 px @2x); tvOS flips and blurs it to fit 1920 pixels at 16:9.
  - Avoid implying interactivity in a static image.
  - Carousel actions: Provide a title (show, movie, or album title) and optionally a brief subtitle (date range, show name).
  - Carousel details: Provide a title that identifies the currently playing content near the top of the screen, optionally with an attribution phrase like "Featured on My App".
  - Sectioned content row: Provide enough content to constitute a complete row spanning the full screen width, with at least one label. Image sizes: Poster (2:3) actual 404x608 pt, focused/safe 380x570 pt, unfocused 333x570 pt; Square (1:1) actual 608x608 pt, focused/safe 570x570 pt, unfocused 500x500 pt; 16:9 actual 908x512 pt, focused/safe 852x479 pt, unfocused 782x440 pt (all @1x with @2x doubled). Be aware of additional scaling when combining image sizes; a 16:9 image scales to 500 pixels high next to a poster or square.
  - Scrolling inset banner: Provide three to eight images. If you need text, add it to your image (on a dedicated layer in layered images) and to the accessibility label. Size: actual 1940x692 pt, focused/safe 1740x620 pt, unfocused 1740x560 pt (@2x 3880x1384, 3480x1240, 3480x1120 px).
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.
- **Content/labels:** Succinct titles and subtitles; text in banners must be baked into the image and mirrored in the accessibility label.
- **APIs:** None named on the page beyond the Top Shelf extension (see Apple Design Resources templates).
- **Web equivalent (translation, not Apple guidance):** A hero carousel on a landing page: full-bleed media with a primary Play and a More Info button, three to eight slides, focusable poster rows with labels, no ads or prices, and `alt` text matching any text baked into imagery.
- **Source:** [reference](../references/components/system-experiences/top-shelf.md)

### Watch faces
- **What it is:** A watch face is a view that people choose as their primary view in watchOS.
- **Platforms:** watchos
- **Use it when:**
  - You want to help people discover your app by sharing preconfigured watch faces that feature your complications (from your app, website, Messages, Mail, or social media).
- **Don't use it when / use instead:**
  - You have no complications to showcase; build [Complications](../references/components/system-experiences/complications.md) first.
  - You target any platform other than watchOS.
- **Rules:**
  - Help people discover your app by sharing watch faces that feature your complications; support multiple complications for a curated experience, and specify accent color, images, or styles where supported. The system prompts people to install your app if needed.
  - Display a preview of each watch face you share, obtained by emailing the face to yourself from the iOS Watch app, optionally composited onto a hardware bezel from Apple Design Resources.
  - Aim to offer shareable watch faces for all Apple Watch devices; some faces (California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact, Solar Dial) require Series 4 and later, and Explorer requires Series 3 with cellular, so offer a similar configuration on an older-compatible face and label each face with the devices it supports.
  - Respond gracefully if people choose an incompatible watch face; offer an alternative configuration instead of an error and set expectations in your previews.
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, tvOS, or visionOS.
- **Content/labels:** Label each shareable face with supported devices.
- **APIs:** Sharing an Apple Watch face (ClockKit).
- **Web equivalent (translation, not Apple guidance):** No direct equivalent; the closest is a "share this configuration" link or file download with a preview image and a clear list of supported devices.
- **Source:** [reference](../references/components/system-experiences/watch-faces.md)

### Widgets
- **What it is:** A widget provides quick access to essential information and focused interactions from your app or game in additional contexts.
- **Platforms:** ios, ipados, macos, watchos, visionos
- **Use it when:**
  - You can show timely, glanceable content tied to your app's main purpose on the Home Screen, Lock Screen, desktop, Notification Center, Smart Stack, visionOS surfaces, or Apple HomeView.
  - Simple interactions (buttons, toggles) or deep links add value without launching the app.
- **Don't use it when / use instead:**
  - You need real-time updates for a time-bound event; use [Live Activities](../references/components/system-experiences/live-activities.md).
  - The widget would only replicate your app icon or static content.
  - You need an action from Control Center or the Action button; use [Controls](../references/components/system-experiences/controls.md).
- **Rules:**
  - Choose simple ideas that relate to your app's main purpose with timely content and relevant functionality.
  - Aim to create a widget that gives people quick access to the content they want; replicating an app icon offers little value.
  - Prefer dynamic information that changes throughout the day.
  - Look for opportunities to surprise and delight (special treatments on birthdays or holidays).
  - Offer widgets in multiple sizes when doing so adds value; don't just stretch a small widget's content, and prefer one great size over all sizes.
  - Balance information density; essential information at a glance, details on a longer look.
  - Display only the information that's directly related to the widget's main purpose.
  - Use brand elements thoughtfully; a small logo in the top-right corner is sufficient when needed.
  - Choose between automatically displaying content and letting people customize displayed information (Stocks configurable, Podcasts automatic).
  - Avoid mirroring your widget's appearance within your app.
  - Let people know when authentication adds value ("Sign in to view reservations").
  - Keep your widget up to date with an appropriate refresh frequency; consider showing when data was last updated.
  - Use system functionality to refresh dates and times in your widget.
  - Use animated transitions to bring attention to data updates, with durations up to two seconds.
  - Offer simple, relevant functionality and reserve complexity for your app.
  - Ensure that a widget interaction opens your app at the right location.
  - Offer interactivity while remaining glanceable and uncluttered; avoid app-like layouts and keep targets large; inline accessory widgets offer only one tap target.
  - In general, use standard margins to ensure legibility: 16 points for most widgets, 11 points for tighter content groupings; margins are smaller on the Mac desktop and the Lock Screen including StandBy.
  - Coordinate the corner radius of your content with the corner radius of the widget using `ContainerRelativeShape`.
  - Prefer using the system font, text styles, and SF Symbols; a custom font works for large text with SF Pro for smaller text.
  - Avoid very small font sizes; display text at 11 points or larger.
  - Avoid rasterizing text.
  - Use color to enhance a widget's appearance without competing with its content.
  - Convey meaning without relying on specific colors to represent information; widgets can be monochrome and watchOS may invert colors.
  - Use full-color images judiciously; reserve them for media content like album art and keep them smaller than the widget.
  - Full-color mode: Support light and dark appearances with semantic colors or asset variants.
  - Accented mode: Group widget components into an accented and a primary group; on iPhone, iPad, and Mac both tint white, on Apple Watch primary is white and accented takes the watch face color.
  - Vibrant mode: Offer enough contrast to ensure legibility; brighter grays give more contrast. Create optimized assets for the best vibrant effect using full opacity, white or light gray for prominent content and darker grays for secondary.
  - Design a realistic preview to display in the widget gallery, using real or realistic simulated data.
  - Design placeholder content that helps people recognize your widget using static components plus semi-opaque shapes for dynamic content.
  - Write a succinct widget description beginning with an action verb ("See the current weather conditions and forecast for a location"); avoid "This widget shows…" or "Add this widget."
  - Group your widget's sizes together, and provide a single description.
  - Consider coloring the Add button in the widget gallery with your brand color.
- **Platform notes:**
  - macOS: No additional considerations. Not supported in tvOS.
  - Sizes and contexts: System small (iPhone Home Screen, Today View, StandBy, CarPlay, Apple HomeView; iPad Home Screen, Today View, Lock Screen; Mac desktop and Notification Center; Vision Pro surfaces), medium and large (Home Screen and Today View on iPhone and iPad; Mac; Vision Pro), extra large (iPad, Mac, Vision Pro), extra large portrait (Vision Pro only). Accessory circular and rectangular (iPhone and iPad Lock Screen; watch complications and Smart Stack), accessory inline (Lock Screen; watch complications), accessory corner (watch complications only). Rendering modes: full color, accented, vibrant per the platform table on the reference page.
  - iOS, iPadOS: Lock Screen widgets follow complication principles too; provide useful information and don't treat them as another launcher. Three Lock Screen styles: inline text above the clock, circular and rectangular below it. Support the Always-On display on iPhone with enough gray-level contrast. Offer Live Activities to show real-time updates. StandBy and CarPlay: two small widgets side by side scaled up with the background removed; Limit usage of rich images or color to convey meaning in StandBy, scale up and rearrange text, and mark the background as removable. Low light renders a monochrome red tint. Apple HomeView: small system widgets on the Modular face (up to four, one face per household, shared across members) and personalized Home Screen.
  - visionOS: Widgets are 3D objects placed on horizontal or vertical surfaces that persist across restarts, with real-world scale. Adapt your design and content for the spatial experience (Music's poster appearance). Test your widgets across the full range of system color palettes and in different lighting conditions. Design a responsive layout that shows the right level of detail for the simplified (distant) and default (nearby) thresholds, removing interactive elements when far. Offer widget family sizes that fit a person's surroundings well. Display content in a way that remains legible from a range of distances; people can scale widgets from 75 to 125 percent. Mounting styles: Choose the mounting style that fits your content; elevated (default, horizontal and vertical surfaces) for present content, recessed (vertical only) for ambient content, declared with `supportedMountingStyles(_:)`. Test your elevated widget designs with each system-provided frame width. Treatment styles: Choose the paper style for a print-like look that responds to lighting; Choose the glass style for information-rich widgets whose foreground stays bright.
  - watchOS: Provide a colorful background that conveys meaning (Stocks: red falling, green rising) instead of the default black. Encourage the system to display or elevate the position of your watchOS widget in the Smart Stack with relevancy information (RelevanceKit).
  - Specifications: iOS small/medium/large/circular/rectangular/inline by screen: 430x932 and 428x926: 170x170, 364x170, 364x382, 76x76, 172x76, 257x26; 414x896: 169x169, 360x169, 360x379, 76x76, 160x72, 248x26; 414x736: 159x159, 348x157, 348x357, 76x76, 170x76, 248x26; 393x852 and 390x844: 158x158, 338x158, 338x354, 72x72, 160x72, 234x26; 375x812 and 360x780: 155x155, 329x155, 329x345, 72x72, 157x72, 225x26; 375x667: 148x148, 321x148, 321x324, 68x68, 153x68, 225x26; 320x568: 141x141, 292x141, 292x311 (no accessory sizes). iPadOS canvas/device sizes (small, medium, large, extra large): 768x1024 and 744x1133 canvas 141x141, 305.5x141, 305.5x305.5, 634.5x305.5 and device 120x120, 260x120, 260x260, 540x260; 810x1080 canvas 146x146, 320.5x146, 320.5x320.5, 669x320.5 and device 124x124, 272x124, 272x272, 568x272; 820x1180 and 834x1194 canvas 155x155, 342x155, 342x342, 715.5x342 and device 136x136, 300x136, 300x300, 628x300; 834x1112 canvas 150x150, 327.5x150, 327.5x327.5, 682x327.5 and device 132x132, 288x132, 288x288, 600x288; 954x1373 and 970x1389 (Display Zoom More Space) 162x162, 350x162, 350x350, 726x350; 1024x1366 canvas 170x170, 378.5x170, 378.5x378.5, 795x378.5 and device 160x160, 356x160, 356x356, 748x356; 1192x1590 (More Space) 188x188, 412x188, 412x412, 860x412. visionOS: small 158x158 pt (268x268 mm), medium 338x158 pt (574x268 mm), large 338x354 pt (574x600 mm), extra large 450x338 pt (763x574 mm), extra large portrait 338x450 pt (574x763 mm). watchOS Smart Stack: 152x69.5 (40mm), 165x72.5 (41mm), 176x72.5 (42mm), 173x76.5 (44mm), 184x80.5 (45mm), 194x80.5 (46mm), 198x81.5 (49mm Ultra 3, 4), 191x81.5 (49mm Ultra 1, 2).
- **Content/labels:** Gallery description: action verb first, approachable language, sentence-style capitalization, one description for all sizes. Text at 11 pt or larger, system font preferred.
- **APIs:** WidgetKit, `WidgetRenderingMode.fullColor`, `.accented`, `.vibrant`, `widgetAccentable(_:)`, `ContainerRelativeShape`, `padding(_:_:)`, `Font`, `Font.custom(_:size:)`, `LevelOfDetail.simplified`, `.default`, `WidgetMountingStyle.elevated`, `.recessed`, `WidgetConfiguration.supportedMountingStyles(_:)`, `WidgetTexture.paper`, `.glass` (SwiftUI, WidgetKit); RelevanceKit; App Intents (configurable widgets).
- **Web equivalent (translation, not Apple guidance):** A self-contained dashboard card (`<section aria-labelledby>`) in fixed size variants with 16px (or 11px tight) padding, `border-radius` concentric with inner shapes, text at 11px or larger, a periodic refresh (not real time), one or two inline actions, a deep link on the card body, and a skeleton placeholder while loading; keep meaning independent of color so a monochrome theme still reads.
- **Source:** [reference](../references/components/system-experiences/widgets.md)
