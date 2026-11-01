# Patterns and Inputs

This guide condenses every page in Apple's Human Interface Guidelines under **Patterns** (how an app behaves at common moments: launching, loading, entering data, asking for feedback, sharing, searching, settings, media playback, and so on) and **Inputs** (how an app responds to the ways people control a device: touch, keyboard, pointer, pencil, remote, Digital Crown, eyes, game controllers, and sensors).

Each entry keeps Apple's bold best-practice sentences as short imperative rules, preserves the exact numbers Apple gives, and notes platform differences. Lines marked **Web translation** are this guide's own suggestion for honoring the same rule in a web app; they are not Apple guidance. Every entry links to the faithful copy of Apple's page under `../references/`.

Use the first table to find the pattern for the moment you are designing, then read the full entry before building the feature.

## Which pattern applies

| App moment | Pattern entry |
|---|---|
| First launch, app start, launch screen, splash screen, state restoration | [Launching](#launching), [Onboarding](#onboarding) |
| Teaching a new user, tutorial, tips, "what's new" | [Onboarding](#onboarding), [Offering help](#offering-help) |
| Sign-in, account creation, passkeys, biometrics, account deletion | [Managing accounts](#managing-accounts) (see also Sign in with Apple in technologies.md) |
| Asking for permission (location, motion, notifications, hands) | [Onboarding](#onboarding) (request during onboarding only if required to function), [Managing notifications](#managing-notifications), [Gyroscope and accelerometer](#gyroscope-and-accelerometer) |
| Empty state, waiting for content, placeholders, spinner vs progress bar | [Loading](#loading), [Feedback](#feedback) |
| Long operation, download, background task | [Loading](#loading), [Multitasking](#multitasking) |
| Error, warning, success confirmation, status | [Feedback](#feedback) |
| Destructive action, confirming before data loss | [Feedback](#feedback), [Modality](#modality), [Undo and redo](#undo-and-redo), [Drag and drop](#drag-and-drop) |
| Modal sheet, alert, popover, full-screen task | [Modality](#modality) |
| Forms, text fields, pickers, validation, passwords | [Entering data](#entering-data) |
| Search field, suggestions, scope, Spotlight indexing | [Searching](#searching) |
| Preferences, options, settings window | [Settings](#settings) |
| Share button, collaboration, invite others | [Collaboration and sharing](#collaboration-and-sharing) |
| Push and local notifications, Focus, Time Sensitive, marketing messages | [Managing notifications](#managing-notifications) |
| Undo, redo, shake to undo, Edit menu | [Undo and redo](#undo-and-redo) |
| Full-screen media or distraction-free mode | [Going full screen](#going-full-screen), [Playing video](#playing-video) |
| Playing music, sound effects, audio session category, interruptions | [Playing audio](#playing-audio) |
| Video player, Picture in Picture, TV app integration | [Playing video](#playing-video), [Live-viewing apps](#live-viewing-apps) |
| Live TV, EPG, channel guide, cloud DVR | [Live-viewing apps](#live-viewing-apps) |
| Vibration, tactile feedback, Taptic Engine | [Playing haptics](#playing-haptics) |
| Charts, graphs, data visualization | [Charting data](#charting-data) |
| Documents, open and save, Files, Finder, Quick Look | [File management](#file-management) |
| Print command, print panel | [Printing](#printing) |
| Moving or copying content between views or apps | [Drag and drop](#drag-and-drop) |
| Asking for an App Store rating | [Ratings and reviews](#ratings-and-reviews) |
| App switching, split view, windows, Picture in Picture | [Multitasking](#multitasking) |
| Fitness tracking, workout session, Activity rings | [Workouts](#workouts) |
| Keyboard shortcuts, Full Keyboard Access | [Keyboards](#keyboards) |
| Mouse, trackpad, pointer effects, cursors | [Pointing devices](#pointing-devices) |
| Touch gestures, custom gestures | [Gestures](#gestures) |
| Apple Pencil drawing, handwriting, Scribble | [Apple Pencil and Scribble](#apple-pencil-and-scribble) |
| Game input, virtual controls, controllers | [Game controls](#game-controls) |
| Apple TV remote | [Remotes](#remotes), [Focus and selection](#focus-and-selection) |
| Apple Watch crown, Vision Pro crown | [Digital Crown](#digital-crown) |
| Looking at UI on Vision Pro, hover effects | [Eyes](#eyes) |
| Action button on iPhone or Apple Watch Ultra | [Action button](#action-button) |
| Camera Control on iPhone 16 | [Camera Control](#camera-control) |
| Ultra Wideband, proximity between devices | [Nearby interactions](#nearby-interactions) |
| Device motion, shake, tilt | [Gyroscope and accelerometer](#gyroscope-and-accelerometer) |

## Patterns

### Charting data
- **Summary:** Presenting data in a chart can help you communicate information with clarity and appeal.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any screen that shows a trend, a changing quantity, or a comparison across categories as a graphic.
  - Deciding whether data belongs in a chart at all, or in a list or table people can scroll, search, and sort.
  - Multiple charts that share a dataset or a purpose and need consistent styling.
- **Rules:**
  - Use a chart when you want to highlight important information about a dataset; if you only need to provide data without helping people analyze it, offer a list or table instead.
  - Keep a chart simple, letting people choose when they want additional details; reveal large datasets or functionality gradually (levels of detail, subsets, progressively richer versions of the chart).
  - Make every chart in your app accessible: provide accessibility labels that describe chart values and components, and accessibility elements that help people interact with the chart.
  - In general, prefer using common chart types such as bar charts and line charts.
  - If you need to create a chart that presents data in a novel way, help people learn how to interpret the chart (Activity introduces its rings by animating them individually).
  - Examine the data from multiple levels or perspectives (macro totals and averages, mid-level subsets, individual data points) to find details you can display to enhance the chart.
  - Aid comprehension by adding descriptive text to the chart: titles, subtitles, annotations, and a headline or summary ("Chance of light rain in the next hour"). A descriptive headline doesn't take the place of accessibility labels.
  - Match the size of a chart to its functionality, topic, and level of detail; large enough to read labels and support interactivity, or deliberately small for glanceable information or a preview of a larger chart.
  - Prefer consistency across multiple charts, deviating only when you need to highlight differences.
  - Maintain continuity among multiple charts that use the same data: one chart type and consistent colors, annotations, layouts, and descriptive text, so the expanded version of a small chart uses the same style, colors, marks, and annotations.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Use descriptive titles, subtitles, annotations, and a brief headline or summary above the chart that states the actionable takeaway.
- **APIs:** Swift Charts (Chart3D for 3D charts); Charts component guidance.
- **Web translation:** Prefer familiar chart types, add a text headline and `aria` descriptions or a data table alternative for every chart, and keep one visual system across all charts on the site. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/charting-data.md)

### Collaboration and sharing
- **Summary:** Great collaboration and sharing experiences are simple and responsive, letting people engage with the content while communicating effectively with others.
- **Platforms:** ios, ipados, macos, visionos, watchos
- **When this applies:**
  - Any app with a Share button, share sheet, or sharing popover.
  - Apps where multiple people edit the same content (CloudKit, iCloud Drive, or a custom collaboration backend).
  - Apps that want Messages integration for invitations and activity notifications (requires universal links for custom infrastructure).
- **Rules:**
  - Place the Share button in a convenient location, like a toolbar, to make it easy for people to start sharing or collaborating. In SwiftUI, present a share link that opens the system share sheet.
  - If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports; include a file (or a plain text representation) in your collaboration object so "send copy" is available.
  - Write succinct phrases that summarize the sharing permissions you support ("Only invited people can edit", "Everyone can make changes"); the system shows your summary in a button that reveals sharing options.
  - Provide a set of simple sharing options that streamline collaboration setup (who can access, edit or read only, whether collaborators can add participants); keep custom choices to a minimum and group them so people understand them at a glance.
  - Prominently display the Collaboration button as soon as collaboration starts; it works well to place it next to the Share button.
  - Provide custom actions in the collaboration popover only if needed. The popover has three sections: collaborators plus Messages and FaceTime buttons on top, your custom items in the middle, and a manage-shared-file button at the bottom. Offer only the most essential items.
  - If it makes sense in your app, customize the title of the modal view's collaboration-management button (default title "Manage Shared File"). CloudKit provides the management view; otherwise you create your own.
  - Consider posting collaboration event notifications in Messages (content change, membership change, mention) including a universal link that opens the relevant view in your app.
  - Support universal links if you use a custom collaboration infrastructure.
- **Platform notes:**
  - iOS, iPadOS, macOS: no additional considerations. iOS 16 share sheet and iPadOS 16 / macOS 13 sharing popover include file-sharing method and permissions for a new collaboration. Not available in tvOS.
  - visionOS: the system streams the current window to collaborators while the app is in the Shared Space; moving to a Full Space pauses the stream until the app returns.
  - watchOS: use ShareLink in SwiftUI to present the system share sheet.
- **Copy/labels:** Permission summaries are short phrases such as "Only invited people can edit" or "Everyone can make changes." Default management button title is "Manage Shared File"; customize only when it makes sense.
- **APIs:** ShareLink (SwiftUI), Shared with You (SWHighlightEvent), CloudKit sharing, iCloud Drive, universal links, Activity views.
- **Web translation:** Put a Share action in the primary toolbar, use the Web Share API where available, describe permission levels in one plain phrase, and show a persistent "shared with" indicator next to Share once a document is shared. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/collaboration-and-sharing.md)

### Drag and drop
- **Summary:** Using drag and drop, people can move or duplicate selected photos, text, and other content by dragging the selection from one location to another.
- **Platforms:** ios, ipados, macos, visionos
- **When this applies:**
  - Any view with selectable content that could be moved or copied within a container, between containers, or between apps.
  - Lists, collections, tables, text views, and canvases that accept dropped items.
  - Multi-item selection and reordering.
- **Rules:**
  - As much as possible, support drag and drop throughout your app; system text fields and text views give it to you for free.
  - Offer alternative ways to accomplish drag-and-drop actions, such as menu commands for copy and move; in iOS and iPadOS use accessibility APIs (`accessibilityDragSourceDescriptors`, `accessibilityDropPointDescriptors`) to identify sources and destinations.
  - Determine when dragging within your app results in a move or a copy: same container moves, different container copies, between apps always copies. Prefer the behavior least likely to cause frustration or data loss.
  - Support multi-item drag and drop when it makes sense; in iPadOS people can add items to an in-progress drag.
  - Prefer letting people undo a drag-and-drop operation; ask for confirmation before a drop that can't be undone, or provide a way to reverse the result.
  - Consider offering multiple versions of dragged content, ordered from highest to lowest fidelity (for example PDF vector, lossless PNG with transparency, lossy JPEG).
  - Consider supporting spring loading so people can activate buttons and segmented controls by dragging content over them (force click on Mac trackpad, hover on iPad).
  - Providing feedback: display a drag image as soon as people drag a selection about three points; make it translucent and show it until the drop.
  - If it adds clarity, modify the drag image to help people predict the result (expand to default size, use flocking to group multiple items); avoid a constantly, radically changing drag image.
  - Show people whether a destination can accept dragged content: show an insertion point or highlight only when it can; show nothing or an explicit "not allowed" image like `circle.slash` when it can't; highlight only while content is over the destination; help identify one destination at a time.
  - When people drop an item on an invalid destination, or when dropping fails, provide visual feedback (slide back to source, or scale up and fade out).
  - Accepting drops: scroll the contents of a destination when necessary as people drag within a scrolling container.
  - When there's a choice, pick the richest version of dropped content your app can accept.
  - Extract only the relevant portion of dropped content if necessary (Mail shows only name and email from a dropped contact).
  - When a physical keyboard is attached, check for the Option key at drop time; Option forces a same-container drag to copy.
  - Provide feedback when dropped content needs time to transfer (progress indicator, placeholder at the drop location).
  - Provide feedback when dropped content initiates a task or action, such as printing.
  - Apply appropriate styling to dropped text: keep the source style when both support it, otherwise apply the destination's style.
  - After a drop, maintain the content's selection state in the destination, updating it in the source as needed (remove selection in the source on a copy, deselect in the source when moving to another container).
- **Platform notes:**
  - iOS, iPadOS: let people perform multiple simultaneous drag activities; support adding items during a drag with flocking feedback and accept multiple simultaneous drops.
  - macOS: consider letting people drag content into the Finder in a format your app can open later (Calendar exports `.ics`; text becomes a clipping). Let people drag a background selection from an inactive window without activating it, and drag individual items from an inactive window without affecting the background selection. Consider a badge (filled oval with a number) during multi-item drags and update it if a destination accepts only a subset. Consider changing the pointer (copy, drag link, disappearing item, operation not allowed). Let people select and drag with a single motion.
  - visionOS: when possible, launch your app to handle content dropped into empty space by associating an NSUserActivity with draggable content. Pinch and hold moves objects in any direction including the z-axis.
  - Not supported in tvOS or watchOS.
- **Copy/labels:** Use the SF Symbol `circle.slash` for a not-allowed drop indicator; macOS multi-item badge shows a count.
- **APIs:** UIKit Drag and drop, AppKit Drag and Drop, File Provider, NSUserActivity, `accessibilityDragSourceDescriptors`, `accessibilityDropPointDescriptors`, Universal Control.
- **Web translation:** Use the HTML Drag and Drop API with a translucent drag image, highlight valid drop zones only while hovered, animate failed drops back, offer multiple MIME types ordered richest first, keep a keyboard or menu alternative, and make the result undoable. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/drag-and-drop.md)

### Entering data
- **Summary:** When you need information from people, design ways that make it easy for them to provide it without making mistakes.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any form, sign-up flow, checkout, or screen with text fields, pickers, or numeric entry.
  - Password or sensitive-data entry.
  - Deciding whether to ask at all, or to obtain the value from the system or by permission.
- **Rules:**
  - Get information from the system whenever possible; don't ask people to enter what you can gather automatically (settings) or by permission (location, calendar).
  - Be clear about the data you need: show a prompt in the field ("username@company.com") or an introductory label ("Email"), and prefill fields with reasonable default values.
  - Use a secure text-entry field when appropriate for sensitive data (displays a filled circle per character). In tvOS configure a digit entry view with `isSecureDigitEntry`; in visionOS the system shows entered data to the wearer only and blurs secure fields during AirPlay.
  - Never prepopulate a password field; always ask people to enter their password or use biometric or keychain authentication.
  - When possible, offer choices instead of requiring text entry: use a picker, menu, or other selection component.
  - As much as possible, let people provide data by dragging and dropping it or by pasting it.
  - Dynamically validate field values and give feedback as soon as you detect a problem; use a number formatter for numeric data (decimal places, percentage, currency).
  - When data entry is necessary, make sure people understand that they must provide the required data before they can proceed; make a Next or Continue button available only after the required data is entered.
- **Platform notes:**
  - macOS: consider an expansion tooltip to show the full version of clipped or truncated text in a field when the pointer rests on it (also applies to iOS and iPadOS apps running on a Mac).
  - No additional considerations for iOS, iPadOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Placeholder examples like "username@company.com"; labels like "Email"; Next or Continue buttons enabled only when required fields are complete.
- **APIs:** SecureField (SwiftUI), SwiftUI Input events, TVUIKit `TVDigitEntryViewController.isSecureDigitEntry`, number formatters, Text fields, Virtual keyboards.
- **Web translation:** Use correct `type` and `autocomplete` attributes so browsers fill known data, validate inline on blur or input, never prefill `type=password`, prefer `select` or radio groups over free text, and disable the submit button until required fields pass. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/entering-data.md)

### Feedback
- **Summary:** Feedback helps people know what's happening, discover what they can do next, understand the results of actions, and avoid mistakes.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Showing status (sync state, unread counts, last update).
  - Reporting success or failure of an important task, or a command that can't be carried out.
  - Warning before an action that causes unexpected, irreversible data loss.
- **Rules:**
  - Match the significance of the information to the way it's delivered: passive display for status, interruption for a warning about possible data loss.
  - Make sure all feedback is accessible; use multiple channels (color, text, sound, haptics) so people get it when the device is silenced, they look away, or they use VoiceOver.
  - Status: consider integrating status feedback into your interface near the items it describes (Mail shows the most recent update and unread count in the mailbox toolbar) so people don't have to leave their context.
  - Alerts: use alerts to deliver critical, and ideally actionable, information. Alerts disrupt the current context, so match importance to the level of interruption; overuse makes them lose impact.
  - Warnings: warn people when they initiate a task that can cause data loss that's unexpected and irreversible. Don't warn when data loss is the expected result (Finder doesn't warn for every file deletion).
  - Confirmations: when it makes sense, confirm that a significant action or task has completed (a successful Apple Pay transaction). Reserve confirmations for sufficiently important activities; people expect success and mostly need to know when something fails.
  - Errors: show people when a command can't be carried out and help them understand why (Maps explains it can't route to and from the same location).
- **Platform notes:**
  - watchOS: avoid displaying an indeterminate progress indicator such as a loading indicator; reassure people they'll receive a notification when the process completes.
  - No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.
- **Copy/labels:** Error messages explain why the command failed; confirmations are reserved for significant actions.
- **APIs:** UIKit Animation and haptics; Alerts component; Playing haptics and Playing audio patterns; Motion.
- **Web translation:** Show status inline near the related element, use modal dialogs only for critical actionable information, confirm only significant actions, explain failures in plain language, and mirror visual feedback with `aria-live` text. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/feedback.md)

### File management
- **Summary:** Some apps can support documents and files that people expect to manage throughout the system.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Document-based apps that create, open, edit, and save files.
  - Apps that need a custom file browser, a document launcher, a file provider extension, or Finder Sync.
  - Showing previews of files, including types your app can't open.
- **Rules:**
  - Creating and opening: use app menus and keyboard shortcuts to give people convenient ways to create and open documents (New, Open in the iPadOS Command-key shortcuts interface and the macOS File menu). Regardless of shortcuts, include an Add (+) button to create a new document; in macOS put the add action in the File menu.
  - If your app requires a custom file browser, support people's understanding of the platform's file system: open to the most relevant location but let people reach the rest of the file system.
  - Saving: help people be confident that their work is always preserved unless they cancel or delete it. Avoid explicit save actions; autosave periodically, on close, and when switching apps.
  - Hide file extensions by default, but let people view them if they choose, and reflect the choice in all save and open interfaces.
  - Quick Look: use a Quick Look viewer to let people preview a file even when your app can't open it.
  - Consider implementing a Quick Look generator if your app produces custom file types so the Finder, Files, and Spotlight can show previews.
- **Platform notes:**
  - iOS, iPadOS (document launcher, iOS 18 and iPadOS 18): a title card with the app title and two app-specific buttons, a background image plus accessory images, and a sheet with a file browser and optional controls. Assign the title card's buttons to your app's most important functions (primary typically creates a new document; Numbers uses Start Writing and Choose a Template). Provide a background that's clearly distinct from the accessories and title card (solid color, gradient, or pattern; avoid complex images). Be mindful of accessory placement so app name and both buttons stay visible; test across screen sizes and orientations. Use animation sparingly (gentle, repeating breathe or sway).
  - iOS, iPadOS (file provider extension): display only documents appropriate in the current context (a PDF editor sees only PDFs); consider showing modification dates, sizes, local vs remote. Let people select a destination when exporting and moving documents, and add subdirectories. Avoid including a custom top toolbar; the modal view already has one.
  - macOS: use the default file browser unless you have an important reason for a custom one. Make a custom file-opening interface convenient (open recent, filters, multi-select; customize the Open button title such as Insert). Provide a save interface to change name, format, or location; new documents are "Untitled" until named; offer a format choice if you support several. Consider extending the Save dialog with an accessory view (Mail offers include attachments). Finder Sync extensions can show sync badges, contextual menu items, and toolbar buttons. Help people avoid losing work if they turn off autosaving ("Ask to keep changes when closing documents"): show unsaved changes and present a save dialog on close, quit, log out, or restart. When autosaving is off, show a dot on the close button and next to the document name in the Window menu; when autosaving is on, don't show the dot. You may append "Edited" to the title and remove it as soon as autosave or explicit save occurs.
  - No additional considerations for tvOS, visionOS, or watchOS (watchOS and tvOS don't provide a document-browsing interface).
- **Copy/labels:** New documents are titled "Untitled"; title bar may show "Edited"; Open button may be retitled to the task (for example Insert); document launcher buttons describe actions (Start Writing, Choose a Template).
- **APIs:** DocumentGroupLaunchScene and Documents (SwiftUI), File Provider, Finder Sync, Quick Look, UIKit document browser, Toolbars, File menu.
- **Web translation:** Autosave continuously and show a subtle "Saved" or "Edited" state instead of a Save button, offer New and Open in the primary toolbar with standard shortcuts, hide extensions by default, and show inline previews for attachments the app can't edit. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/file-management.md)

### Going full screen
- **Summary:** iPhone, iPad, and Mac offer full-screen modes that let people expand a window to fill the screen, hiding system controls and providing a distraction-free environment.
- **Platforms:** ios, ipados, macos
- **When this applies:**
  - Games, media viewing (video, photo slideshows), reading, and in-depth focused tasks.
  - Any screen that temporarily hides toolbars and navigation to prioritize content.
  - Deciding how the Dock and Home Screen indicator behave while your app is full screen.
- **Rules:**
  - Support full-screen mode when it makes sense for your experience (games, media, distraction-free tasks).
  - If necessary, adjust your layout in full-screen mode, but don't programmatically resize your window; keep adjustments subtle to avoid jarring transitions.
  - Continue to provide access to essential features and controls so people can complete their task without exiting (playback controls persistently available or easy to reveal).
  - Except in games, let people reveal the Dock while your iPadOS or macOS app is in full-screen mode; in a game you can ask iPadOS to ignore an initial swipe up from the bottom edge or hide the Dock in macOS.
  - After people switch away from your full-screen experience, help them resume where they left off (pause a game or slideshow automatically).
  - Let people choose when to exit full-screen mode; don't end it automatically when they switch away or finish an activity.
  - Prioritize content by temporarily hiding toolbars and navigation controls, and let people restore them with a familiar gesture (tap, swipe down, move the cursor to the top). Keep controls visible when they're essential for navigation or tasks.
- **Platform notes:**
  - iOS, iPadOS: consider deferring system gestures to prevent accidental exits. By default the Home Screen indicator hides shortly after switching to your app and reappears on interaction with the bottom of the screen, allowing one swipe to exit; retain this when possible, or enable two swipes rather than one if it causes unexpected exits.
  - macOS: use the system-provided full-screen experience (accommodates the camera housing). In a game, don't change the display mode when players go full screen. Always let people choose when to enter full-screen mode via the window's Enter Full Screen button, View menu item, or Control-Command-F; avoid a custom menu of window modes; a game may offer a custom toggle.
  - Not supported in tvOS, visionOS, or watchOS (Apple TV and Apple Watch fill the screen by default; Vision Pro uses immersion via the Digital Crown).
- **Copy/labels:** macOS menu item is "Enter Full Screen" with shortcut Control-Command-F.
- **APIs:** `fullScreenCover(item:onDismiss:content:)` (SwiftUI), `preferredScreenEdgesDeferringSystemGestures` (SwiftUI UIHostingController and UIKit), `hideDock` presentation option and `toggleFullScreen(_:)`, NSScreen, NSWindow.CollectionBehavior (AppKit), Managing your game window for Metal in macOS.
- **Web translation:** Use the Fullscreen API only on an explicit user action, keep playback or task controls reachable by tap or mouse movement, pause media when the tab loses visibility, and never exit fullscreen programmatically except on user request. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/going-full-screen.md)

### Launching
- **Summary:** A streamlined launch experience helps people start using your app or game immediately.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - App start, initial download, and the moment before the first screen appears.
  - Designing the launch screen required by iOS, iPadOS, and tvOS.
  - Deciding where a splash screen goes and how to restore previous state.
- **Rules:**
  - Launch instantly; people sometimes don't want to wait more than a couple of seconds.
  - If the platform requires it, provide a launch screen (iOS, iPadOS, tvOS). macOS, visionOS, and watchOS don't require one.
  - If you need a splash screen, consider displaying it at the beginning of your onboarding flow, or as soon as launching completes if there's no onboarding.
  - Restore the previous state when your app restarts (scroll position, windows in the same state and location) so people continue where they left off.
  - Launch screens: downplay the launch experience; its sole function is to make the app seem quick to launch and immediately ready.
  - Design a launch screen that's nearly identical to the first screen of your app or game; if the first screen shows a solid color, the launch screen shows only that color; match the device's orientation and appearance mode.
  - Avoid including text on your launch screen, even if your first screen displays text, because it won't be localized.
  - Don't advertise; the launch screen isn't a branding opportunity, splash screen, or About window; include logos only if they're a fixed part of the first screen.
- **Platform notes:**
  - iOS, iPadOS: launch in the appropriate orientation (the device's current one if both are supported; otherwise the supported one, responding correctly to left or right rotation).
  - tvOS: the launch screen is static, unlike layered images elsewhere. In a live-viewing app, consider automatically starting playback soon after people start the app (after a few seconds of inactivity).
  - visionOS: consider launching in the Shared Space even if your app is fully immersive, to give context, load time, and a control people use to open the immersive experience.
  - No additional considerations for macOS or watchOS.
- **Copy/labels:** No text on launch screens.
- **APIs:** Specifying your app's launch screen (Xcode), Responding to the launch of your app (UIKit).
- **Web translation:** Make the first paint match the loaded layout (skeleton in the final structure, no logo interstitial), restore scroll and route state on reload, and keep time-to-interactive within a couple of seconds. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/launching.md)

### Live-viewing apps
- **Summary:** As you design a live-viewing app, prioritize the content and create fun, fluid interactions that encourage immersion in the live-viewing experience.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Apps that stream live TV, sports, or channel-based content alongside video on demand.
  - Electronic program guides (EPG) and channel browsing during playback.
  - Cloud DVR recording features.
- **Rules:**
  - Feature live content prominently and make it easy to access; with live content in the first tab, people tap no more than once to start viewing.
  - Let people tap once, or not at all, to start playback (a Watch Now button on featured content that disappears into full-screen playback).
  - Make sure live content looks live: a "Live" collection row and a badge, symbol, or sash on each live item.
  - Consider indicating the progress of currently playing live content with a progress bar.
  - Give people additional actions and viewing alternatives; playback is always primary. Display actions in the same order throughout (for example Watch, Start Over, Record, and Favorite). Show when content airs again.
  - Consider using a content footer for browsing channels during playback: give it a subtle darkening treatment, badge or tint the current thumbnail, match EPG categories, and make invoke and dismiss symmetric (swipe up to show, swipe down to hide).
  - Provide instant visual feedback when people change channels (confirms arrival and covers load time).
  - Match audio to the current context: audio continues while browsing within the live context, but stops when people navigate away from the live tab.
  - EPG: prominently display current information (program, channel, time) and make it easy to return to playback.
  - Make browsing the EPG effortless (page, scroll, jump; a My Channels or Favorites group).
  - Group content into familiar categories (Movies, TV Shows, Kids, Sports, Popular), matching the content footer.
  - Let people browse the EPG without leaving their current content (Picture in Picture or background playback).
  - Cloud DVR: let people start and stop recording from the info panel; let them record a future program from its detail view, choosing only that program or all future episodes; help people adapt recording (current episode, new episodes, specific teams); allow playback, deletion, and recording settings within the cloud DVR area; consider a control to manage DVR settings, including automatic storage management that overwrites the oldest or already viewed content.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Row title "Live"; a "Watch Now" button; consistent action order such as Watch, Start Over, Record, Favorite; categories like Movies, TV Shows, Kids, Sports, Popular.
- **APIs:** Remotes input guidance; Playing video pattern; (tvOS channel navigation via TVServices is referenced from Remotes).
- **Web translation:** Autoplay or one-click play for the live stream on the landing view, badge live items consistently, keep a persistent progress indicator, and let a guide overlay open over the player without stopping playback. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/live-viewing-apps.md)

### Loading
- **Summary:** The best content-loading experience finishes before people become aware of it.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any time content, assets, or levels aren't immediately available (network fetch, large downloads, game levels).
  - Choosing between determinate and indeterminate progress indicators.
  - Installation and first-launch asset downloads.
- **Rules:**
  - Show something as soon as possible: placeholder text, graphics, or animations that are replaced as content arrives, so people don't read a blank view as a problem.
  - Let people do other things in your app or game while they wait for content to load; load in the background.
  - If loading takes an unavoidably long time, give people something interesting to view while they wait (gameplay hints, tips, new features); gauge remaining time accurately so placeholder content is neither cut off nor repeated.
  - Improve installation and launch time by downloading large assets in the background with the Background Assets framework (level packs, 3D models, textures) right after installation, during updates, or at other nondisruptive times.
  - Clearly communicate that content is loading and how long it might take: use a determinate progress indicator when you know the duration and an indeterminate one when you don't, for anything that takes more than a moment or two.
  - For games, consider creating a custom loading view that matches the game's style.
- **Platform notes:**
  - watchOS: as much as possible, avoid showing a loading indicator; display content immediately. If content needs a second or two, a loading indicator is better than a blank screen.
  - No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.
- **Copy/labels:** Tips and hints shown during long loads should be relevant to the app or game.
- **APIs:** Background Assets, Apple-Hosted Background Assets, Progress indicators component, GameKit guidance for large downloads.
- **Web translation:** Render skeleton placeholders in the final layout immediately, stream content progressively, show a determinate progress bar when size is known and an indeterminate one otherwise, and prefetch heavy assets in the background. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/loading.md)

### Managing accounts
- **Summary:** When it doesn't create an unnecessary barrier to your experience, an account can be a convenient way for people to access their content and track personal details.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Deciding whether to require an account at all and when to ask for sign-in.
  - Sign-in, sign-up, passkeys, biometric authentication, and the wording of authentication buttons.
  - Account deletion (required if you offer account creation), subscriptions, and TV provider sign-in.
- **Rules:**
  - Ask people to create an account only if your core functionality requires it; otherwise let people use the app without one. If you require an account, consider Sign in with Apple.
  - Explain the benefits of creating an account and how to sign up, in a brief, friendly description displayed in your sign-in view.
  - Delay sign-in for as long as possible (a shopping app lets people browse and asks only at purchase).
  - If you don't use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey; if you must keep passwords, require two-factor authentication.
  - Always identify the authentication method you offer ("Sign In with Face ID" rather than "Sign In").
  - Refer only to authentication methods that are available in the current context (check LABiometryType; don't mention Face ID on a device without it).
  - In general, avoid offering an app-specific setting for opting in to biometric authentication; people enable it at the system level.
  - Avoid using the term "passcode" to refer to account authentication; it means the device unlock code.
  - Deleting accounts: if you help people create an account, you must also help them delete it, not just deactivate it, and comply with regional legal requirements. If law compels you to keep accounts or information (digital health records) or follow a specific process, clearly describe the situation.
  - Provide a clear way to initiate account deletion within your app; if you can't, provide a direct, easy-to-find link to the webpage (don't bury it in Privacy Policy or Terms of Service). If people used Sign in with Apple, revoke the tokens on deletion.
  - Provide a consistent account-deletion experience in-app and on the website.
  - Consider letting people schedule account deletion to occur in the future, and also offer immediate deletion.
  - Tell people when account deletion will complete, and notify them when it's finished.
  - If you support in-app purchases, help people understand how billing and cancellation work when they delete their account: subscription billing continues through Apple until they cancel, regardless of account deletion; after deletion they need to cancel or request a refund. Explain how to cancel subscriptions and manage purchases. You must support account deletion even if the subscription wasn't bought in your app.
  - TV provider accounts: use TV Provider Authentication for system-level sign-in. Avoid displaying a sign-out option when people are signed in at the system level; if required, prompt them to go to Settings > TV Provider. Never instruct people to sign out by adjusting privacy controls (Settings > Privacy manages app access, not sign-out).
- **Platform notes:**
  - tvOS: ask for the minimum information. Prefer letting people use another device to sign up or authenticate (associated domains, Sign in with Apple). When people are signed in to a shared account, avoid asking them to choose their profile every time (tvOS 16 shares credentials while storing per-user profiles). Minimize data entry; for more than a small amount, send people to a website on another device; for email, show the email keyboard with recent addresses.
  - watchOS: use iCloud synchronization to provide Keychain access for autofill and preserved settings.
  - No additional considerations for iOS, iPadOS, macOS, or visionOS.
- **Copy/labels:** Name the method: "Sign In with Face ID", not generic "Sign In". Don't use "passcode" for account authentication. Sign-out guidance for TV providers points to Settings > TV Provider.
- **APIs:** Sign in with Apple, passkeys (Authentication Services, Supporting passkeys), iCloud Keychain Verification Codes, LABiometryType (LocalAuthentication), Sign in with Apple REST token revocation, `kSecUseUserIndependentKeychain`, User Management Entitlement, associated domains, TV Provider Authentication.
- **Web translation:** Let people browse before requiring an account, support passkeys (WebAuthn) first and password plus 2FA second, label the auth method on the button, and expose an in-product account deletion flow (or a direct link) with a clear completion timeline. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/managing-accounts.md)

### Managing notifications
- **Summary:** Notifications can give people timely and important information, whether the device is locked or in use.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any local or remote notification; you need permission before sending any notification.
  - Choosing an interruption level and deciding whether a notification is a communication (calls, messages) or noncommunication notification.
  - Marketing or promotional messages, and the in-app notification settings screen.
- **Rules:**
  - Get permission before sending any notification; the system lets people change this in settings and silence all notifications (except government alerts in some locales).
  - Integrate with Focus and delivery scheduling: a Focus filters notifications during an activity; scheduled delivery groups alerts into a summary. Even if a Focus delays the alert, the notification itself is available as soon as it arrives.
  - Use communication notifications for direct communications like calls and messages (adopt SiriKit intents: INSendMessageIntent, UNNotificationContentProviding); use noncommunication notifications for everything else and specify an interruption level for each.
  - Interruption levels: Passive (view at leisure, like a restaurant recommendation); Active (default; a score update); Time Sensitive (directly impacts the person and requires immediate attention, like an account security issue or package delivery); Critical (urgent health and safety; extremely rare; typically governmental, public agencies, or health and home apps).
  - Behavior table: Passive and Active don't override scheduled delivery, don't break through Focus, and don't override the Ring/Silent switch. Time Sensitive overrides scheduled delivery and breaks through Focus but doesn't override Ring/Silent. Critical overrides all three. You must get an entitlement to send a Critical notification.
  - Build trust by accurately representing the urgency of each notification; don't use a high level to push low-priority information.
  - Use the Time Sensitive interruption level only for notifications that are relevant in the moment: an event happening now or within an hour. The system explains Time Sensitive on first use and periodically lets people turn it off for your app.
  - Marketing: don't use notifications to send marketing or promotional content unless people explicitly agree.
  - Never use the Time Sensitive interruption level to send a marketing notification.
  - Get people's permission if you want to send them promotional or marketing notifications: an alert, modal view, or other interface that describes the information and offers a clear opt in or out.
  - Make sure people can manage their notification settings within your app; you must provide an in-app settings screen to change their choice.
- **Platform notes:**
  - watchOS: iPhone notification settings apply to the same apps on Apple Watch by default; people manage them in the Apple Watch app or per notification (Mute 1 Hour, Turn off Time Sensitive) by swiping left on the watch.
  - No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.
- **Copy/labels:** The opt-in interface for marketing describes the types of information you'll send and offers explicit opt in and opt out.
- **APIs:** User Notifications (UNNotificationInterruptionLevel, UNNotificationContentProviding), SiriKit INSendMessageIntent, Critical alerts entitlement.
- **Web translation:** Request Web Push permission only after an explicit user action that explains the benefit, separate transactional from marketing pushes with a distinct opt-in, never mark marketing as urgent, and provide an in-app notification preferences page. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/managing-notifications.md)

### Modality
- **Summary:** Modality is a design technique that presents content in a separate, dedicated mode that prevents interaction with the parent view and requires an explicit action to dismiss.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Alerts, sheets, popovers, action sheets or confirmation dialogs, activity views, and full-screen modal tasks (editing, markup, camera).
  - Any flow that takes people out of their current context and requires a dismiss action.
  - Deciding whether to stack a second modal on top of a first.
- **Rules:**
  - Present content modally only when there's a clear benefit: critical information, confirming or modifying a recent action, a distinct narrowly scoped task, or an immersive or concentrated experience.
  - Aim to keep modal tasks simple, short, and streamlined so people don't lose track of the task they suspended.
  - Take care to avoid creating a modal experience that feels like an app within your app; if subviews are necessary, provide a single path and avoid buttons that could be mistaken for the dismiss button.
  - Consider using a full-screen modal style for in-depth content or a complex task (videos, photos, camera, marking up a document, editing a photo). In visionOS a full-screen modal fills a window in the Shared Space and can become more immersive in a Full Space.
  - Always give people an obvious way to dismiss a modal view: a button in the top toolbar or swipe down in iOS, iPadOS, and watchOS; a button in the main content view in macOS and tvOS.
  - When necessary, help people avoid data loss by getting confirmation before closing a modal view (for example an iOS action sheet with a save option) whether they dismiss by gesture or button.
  - Make it easy to identify a modal view's task with a title that names the task or additional guidance text.
  - Let people dismiss a modal view before presenting another one. An alert can appear on top of all other content, but never display more than one alert at the same time.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS. Component choice varies: iOS, iPadOS, and macOS tend to use sheets or popovers for tasks; iPadOS, macOS, and visionOS may use a separate window.
- **Copy/labels:** Title the modal view with its task; the dismiss control must be obvious and clearly distinct from other buttons.
- **APIs:** SwiftUI Presentation modifiers, UIModalPresentationStyle (UIKit), Modal Windows and Panels (AppKit); Sheets, Alerts, Popovers, Action sheets, Activity views components.
- **Web translation:** Use the native `dialog` element with a visible Close control and a title, trap focus, confirm before discarding unsaved input, and never open a second modal before the first is dismissed. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/modality.md)

### Multitasking
- **Summary:** Multitasking lets people switch quickly from one app to another, performing tasks in each.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **When this applies:**
  - Every app except rare exceptions (some games, visionOS apps in a Full Space); people expect it to work.
  - Saving and restoring context when the app is backgrounded, resized, or windowed.
  - Audio interruptions, background tasks, and notifications about finished tasks.
- **Rules:**
  - Always be prepared to save and restore context, because you don't know when people will multitask.
  - Pause activities that require people's attention or active participation when they switch away (games, media viewing), and let them continue as if they never left.
  - Respond smoothly to audio interruptions: pause audio indefinitely for primary interruptions (music, podcasts, audiobooks); temporarily lower volume or pause for shorter interruptions (GPS directions) and resume afterward.
  - Finish user-initiated tasks in the background (downloads, video processing) before suspending if no further input is needed.
  - Use notifications sparingly: notify when an important or time-sensitive task completes; don't notify for routine or secondary tasks.
- **Platform notes:**
  - iOS: FaceTime or Picture in Picture video can continue while people use another app; the app switcher shows open apps.
  - iPadOS: people view and interact with windows of several apps at once; an app can support multiple windows. Apps run full screen or windowed with resizable windows, system window controls for tiling, full screen, minimize, and close; the frontmost window has colored controls and casts a drop shadow. Picture in Picture overlays other content. Apps don't control multitasking configurations or receive any indication of them, so adapt gracefully to different sizes.
  - macOS: multitasking is the default; drop shadows and visual effects distinguish window states.
  - tvOS: people can browse while playing content in Picture in Picture where supported.
  - visionOS: multiple apps run in the Shared Space; only one window is active at a time; the inactive window becomes more translucent and recedes along the z-axis; closing a window backgrounds the app without quitting. Closing the Now Playing app's window pauses audio (resume in Control Center). Avoid interfering with the system-provided multitasking behavior (don't change the appearance of a window's edges, which the system feathers). Don't pause a window's video playback when people look away from it. Be prepared for situations where your audio can duck when people look at another app, unless yours is the Now Playing app.
  - Not supported in watchOS.
- **Copy/labels:** n/a
- **APIs:** Responding to the launch of your app, Multitasking on iPad, Mac, and Apple Vision Pro (UIKit), UISplitViewController, scenes; Windows, Layout, Playing video, Playing audio, Managing notifications.
- **Web translation:** Persist state on `visibilitychange` and `pagehide`, pause games and media when the tab is hidden, support responsive layouts for side-by-side windows, and finish uploads with background sync rather than blocking the user. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/multitasking.md)

### Offering help
- **Summary:** Although the most effective experiences are approachable and intuitive, you can provide contextual help when necessary.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Inline instructions for one- or two-step tasks, tutorials for multistep tasks.
  - Tips (TipKit) that introduce new or less obvious features.
  - Tooltips (help tags) on macOS and visionOS controls.
- **Rules:**
  - Let your app's tasks inform the types of help people might need: inline views for simple tasks, tutorials for complex ones; relate help to what people are doing right now and make it easy to dismiss or avoid.
  - Use relevant and consistent language and images in your help content: match the current input device (don't show a game controller when someone uses the Siri Remote) and platform terms (don't say "click" on iPhone or "tap" on Mac).
  - Make sure all help content is inclusive.
  - Avoid bloating your help content by explaining how standard components or patterns work; describe the specific action a standard element performs in your app; for unique controls or nonstandard input use, prefer animation or graphics over lengthy description.
  - Tips: use the most appropriate tip type (popover tip to preserve content flow, inline tip to keep surrounding information visible; annotation-style inline tip pointing to a UI element, hint-style tip when not tied to specific UI).
  - Use tips for simple features; if a feature requires more than three actions, it's probably too complicated for a tip.
  - Make tips short, actionable, and engaging: direct, action-oriented language; one or two sentences; no promotional content or content about a different feature or flow.
  - Define rules to help ensure your tips reach the intended audience (parameter-based or event-based eligibility); with more than one tip, set display frequency to a reasonable cadence, for example once every 24 hours.
  - If there's an image or symbol people associate with the feature, consider including it in the tip, and prefer the filled variant; don't repeat the same image in both the tip and the UI it points to.
  - Use buttons to direct people to information or options (settings, setup flows, additional resources).
- **Platform notes:**
  - macOS, visionOS (tooltips, called help tags in user documentation): appear when the pointer rests over an element, or in visionOS when a person looks at it. Describe only the control that people indicate interest in. Explain the action or task the control initiates, often starting with a verb ("Restore default settings", "Add or remove a language from the list"). In general, avoid repeating a control's name in its tooltip. Be brief: limit tooltip content to a maximum of 60 to 75 characters; use sentence fragments and omit articles. Use sentence case; omit ending punctuation unless required by your style. Consider offering context-sensitive tooltips for a control's different states.
  - No additional considerations for iOS, iPadOS, tvOS, or watchOS.
- **Copy/labels:** Tips: one or two sentences, action-oriented, no promotion. Tooltips: verb-first, sentence case, 60 to 75 characters maximum, no trailing period, don't repeat the control's name. Use "tap" on touch devices and "click" on Mac.
- **APIs:** TipKit, `help(_:)` (SwiftUI), NSHelpManager (AppKit), Help menu.
- **Web translation:** Use `title` or an accessible tooltip component with verb-first, sentence-case text under 75 characters, show feature tips only once and only to eligible users, cap frequency, and keep tips to two sentences with a single button. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/offering-help.md)

### Onboarding
- **Summary:** Onboarding can help people get a quick start using your app or game.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - After launching completes, when people first use the app or game.
  - Deciding between a single onboarding flow, contextual tips, or an optional tutorial.
  - Deciding when to request permissions, show a splash screen, or ask for ratings and purchases.
- **Rules:**
  - Ideally, people understand your app simply by experiencing it; if onboarding is necessary, make it fast, fun, and optional. Onboarding is not part of launching.
  - Teach through interactivity; let people safely test an action, discover a feature, or try a game mechanic.
  - Consider providing a collection of context-specific tips instead of a single onboarding flow; display instructions near the area of the interface they refer to.
  - If you need to present a prerequisite onboarding flow, design a brief, enjoyable experience that doesn't require people to memorize a lot of information.
  - If it makes sense to offer a separate tutorial, consider making it optional; if people skip it, don't present it again on later launches, but keep it easy to find (help, account, or settings area).
  - Keep onboarding content focused on the experience you provide, not on how to use the system or device.
  - Briefly display a splash screen if necessary, just long enough to absorb at a glance without feeling delayed.
  - Don't let large downloads hinder onboarding; include enough media in the package so people can start immediately.
  - Avoid displaying licensing details within your onboarding flow; let the App Store display agreements and disclaimers; if you must include them, integrate them in a balanced way.
  - Postpone nonessential setup flows or customization steps; provide reasonable defaults.
  - If your app needs access to private data or resources before it can function, consider integrating the permission request into your onboarding flow to show why and the benefits; otherwise request permission when people first access the function that needs it.
  - Prefer letting people experience your app or game before prompting them for ratings or purchases.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Keep instructional copy about your app, not the device; offer a visible Skip for optional tutorials.
- **APIs:** TipKit; Requesting permission (Privacy foundations); Launching pattern.
- **Web translation:** Prefer contextual coach marks over a mandatory carousel, make any tour skippable and re-openable from Help, defer permission prompts (notifications, location) until the feature needs them, and don't put legal text or rating asks in the first session. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/onboarding.md)

### Playing audio
- **Summary:** People expect rich audio experiences that automatically adjust when the context changes on the device.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any app that plays sound: music, podcasts, sound effects, game soundtracks, recording, VoIP.
  - Choosing an audio session category and handling silence mode, volume, headphones, rerouting, and interruptions.
  - Spatial Audio and custom sound design in visionOS; background audio and Now Playing on watchOS.
- **Rules:**
  - Silence: in silent mode play only audio people explicitly initiate (media playback, alarms, audio and video messaging); silence nonessential sounds such as keyboard clicks, sound effects, game soundtracks, and audible feedback.
  - Volume: people expect their volume settings to affect all sound in the system; the exception is ringer volume on iPhone.
  - Headphones: reroute automatically without interruption when connected; pause playback immediately when disconnected.
  - Adjust levels automatically when necessary, but don't adjust the overall volume; the system volume always governs final output.
  - Permit rerouting of audio when possible (living room stereo, car radio, Apple TV).
  - Use the system-provided volume view (MPVolumeView) for volume and output rerouting; you can customize the slider.
  - Choose an audio category that fits the way your app uses sound: Solo ambient (not essential, silences other audio, responds to silence switch, no mixing, no background); Ambient (not essential, mixes, responds to silence switch, no background); Playback (essential, may mix, ignores silence switch, can play in background); Record (ignores silence switch, no mixing, can record in background); Play and record (ignores silence switch, may mix, can record and play in background). Don't make people stop their music if you don't need to.
  - Respond to audio controls only when it makes sense: if your app is actively playing, in a clear audio context, or connected via Bluetooth or AirPlay. Otherwise don't halt another app's audio.
  - Avoid repurposing audio controls; if you don't support a control, don't respond to it.
  - Consider creating custom audio player controls only if you need commands the system doesn't support (custom skip increments, related content like a sports score).
  - Let other apps know when your app finishes playing temporary audio (flag the session with `notifyOthersOnDeactivation`).
  - Determine how to respond to audio-session interruptions (a recorder may avoid interruption for an incoming call unless accepted; a VoIP app must end a call when the iPad Smart Folio closes while using the built-in mic, and must not silently restart the session on reopen).
  - When an interruption ends, determine whether to resume audio playback automatically: media apps check for a resumable interruption (phone call) versus nonresumable (new music playlist); games can resume automatically.
- **Platform notes:**
  - iOS, iPadOS: use the system's sound services (Audio Services) to play short sounds and vibrations.
  - macOS: notification sounds mix with other audio by default.
  - tvOS: the system plays audio only when people initiate it; no sounds accompany alerts or notifications.
  - visionOS: Spatial Audio is everywhere; never communicate important information using only sound. Now Playing audio pauses when its window closes; other apps' audio can duck when people look away. Prefer playing sound (a silent immersive app can feel broken). Design custom sounds for custom UI elements. Use Spatial Audio (ambient audio and audio sources) for an intuitive, engaging experience. Consider defining a range of places from which sounds originate (sound follows a moved window). Consider varying sounds that could feel repetitive by randomizing pitch and volume. Decide whether sound is fixed to the wearer or tracked to an object; generally prefer tracked for realism (Mindfulness uses fixed sound).
  - watchOS: the system manages playback; short clips play in the foreground, longer audio can continue when the wrist lowers. Use the recommended encoding values: 64 kbps HE-AAC. Consider presenting a Now Playing view so people control current or recent audio without leaving your app.
- **Copy/labels:** n/a
- **APIs:** AVAudioSession and AVAudioSession.Category (AVFAudio), `notifyOthersOnDeactivation`, `shouldResume`, Handling audio interruptions, MPVolumeView (MediaPlayer), Audio Services (AudioToolbox), AVFoundation media playback configuration, MusicKit, WatchKit Playing Background Audio and Now Playing view.
- **Web translation:** Never autoplay sound without a user gesture, respect system volume (don't implement your own master gain), pause on device change or tab hide, use the Media Session API so system controls work, and provide visual equivalents for every audio cue. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/playing-audio.md)

### Playing haptics
- **Summary:** Playing haptics can engage people's sense of touch and bring their familiarity with the physical world into your app or game.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any tactile feedback: standard control haptics on iPhone, feedback generators, Core Haptics custom patterns, Apple Watch Taptic Engine, Force Touch trackpad, game controllers, Apple Pencil Pro.
  - Pairing haptics with animation and sound.
  - Offering a way to turn haptics off.
- **Rules:**
  - Use system-provided haptic patterns according to their documented meanings; if a pattern's documented use doesn't fit, use a generic pattern or create your own.
  - Use haptics consistently throughout your app or game so each pattern has a clear cause-and-effect relationship (don't use the same pattern for failure and success).
  - Prefer using haptics to complement other feedback; match the intensity and sharpness of a haptic with the animation it accompanies, and synchronize with sound.
  - Avoid overusing haptics; test to find a balance; the best haptic experience is one people may not notice but miss when it's off.
  - In most apps, prefer playing short haptics that complement discrete events; long-running haptics dilute meaning (on Apple Pencil Pro, continuous haptics can make holding the pencil less pleasant).
  - Make haptics optional: let people turn off or mute haptics and keep the app enjoyable without them.
  - Be aware that playing haptics might impact other user experiences (camera, gyroscope, microphone).
  - Custom haptics (Core Haptics): build from transient events (brief taps, like the Flashlight button) and continuous events (sustained vibration, like the lasers effect); control sharpness (soft and organic versus crisp and mechanical) and intensity (strength); optionally include audio; vary dynamically with input or context.
- **Platform notes:**
  - iOS: standard components (toggles, sliders, pickers) play system haptics by default. Feedback generator categories: Notification (success, warning, error; outcome of a task like depositing a check), Impact (light, medium, heavy, rigid, soft; a view snapping into place or heavy objects colliding), Selection (values changing in a UI element).
  - macOS: with a Magic Trackpad, three patterns for drag or force click: Alignment (dragged item aligns, scaling to fit, reaching min or max of a scrubber), Level change (discrete pressure levels, such as fast-forward speed), Generic (when others don't apply).
  - watchOS: Apple Watch Series 4 and later gives Digital Crown haptic detents. Defined haptics with specific meanings: Notification (something significant requires attention; also plays for notifications), Up (value increased above a threshold), Down (value decreased below a threshold), Success, Failure, Retry (failed but can retry), Start (an activity started; stop usually follows), Stop (an activity stopped), Click (dial clicking at predefined increments; overuse diminishes utility and overlapping clicks confuse).
  - iPadOS, macOS, tvOS, visionOS: game controllers can provide haptic feedback; Apple Pencil Pro and some trackpads provide haptics on certain iPad models.
- **Copy/labels:** Provide a setting labeled for turning haptics off or muting them.
- **APIs:** UIFeedbackGenerator (UIKit), Core Haptics, NSHapticFeedbackPerformer (AppKit), WKHapticType (WatchKit), Playing Haptics on Game Controllers.
- **Web translation:** Use `navigator.vibrate` sparingly on supporting devices for short, discrete events only, tie each pulse to one consistent meaning, pair it with visual feedback, and offer a toggle to disable it. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/playing-haptics.md)

### Playing video
- **Summary:** People expect to enjoy rich video experiences on their devices, regardless of the app or game they're using.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any embedded or full-screen video playback, including Picture in Picture.
  - Apps that surface content through the TV app (handoff, resume, loading, exit behavior).
  - Immersive or inline video on visionOS; short clips on watchOS.
- **Rules:**
  - Playback modes: aspect-fill (full-screen, edge cropping possible) is the default for wide video (2:1 through 2.40:1); aspect (fit-to-screen, letterboxing or pillarboxing) is the default for standard video (4:3, 16:9, anything up to 2:1) and ultrawide (above 2.40:1).
  - Use the system video player to give people a familiar and convenient experience; if you need a custom player, reference the system player's behavior and interface, because slight divergence frustrates people.
  - Always display video content at its original aspect ratio; embedded letterbox or pillarbox padding makes videos appear smaller and breaks edge-to-edge contexts like Picture in Picture on iPad.
  - Provide additional information when it adds value (image, title, description via external metadata) without obscuring playback.
  - Support the interactions people expect regardless of input device: Space on a connected keyboard plays or pauses on Apple Vision Pro, Mac, iPhone, iPad, and Apple TV; familiar Siri Remote gestures on Apple TV.
  - If people need playback options or content-specific information in your tvOS app, consider adding a transport control (playback-related actions like favoriting) or a custom content tab (supplementary information or recommendations); keep actions to a step or two and content succinct.
  - Avoid allowing audio from different sources to mix as viewers switch between modes (handle secondary audio with `silenceSecondaryAudioHintNotification`).
  - TV app integration: ensure a smooth transition (the TV app fades to black and skips your launch screen; immediately present your own black screen before playing).
  - Show the expected content immediately; no splash screens, detail screens, or intro animations; if an interstitial is unavoidable, Select steps through it and Play skips it.
  - Avoid asking people if they want to resume playback; resume automatically.
  - Play or pause playback when people press Space on a connected Bluetooth keyboard.
  - Make sure content plays for the correct viewer: switch to the profile the TV app specifies, or ask the viewer to choose one if none is specified.
  - Use the previous end time when resuming playback of a long video clip.
  - Loading: avoid displaying loading screens when possible; if loading takes more than two seconds, show a black loading screen with a centered activity spinner and no surrounding content. Start playback immediately once enough content loads and keep loading in the background. Minimize loading screen content while keeping the black background.
  - Exiting playback: show a contextually relevant screen (a detail view with a resume option, or a menu listing the content, or the main menu). Be prepared for an immediate exit by preparing the exit view as soon as you receive a playback notification.
- **Platform notes:**
  - tvOS: defer to content when displaying logos or noninteractive overlays; keep overlays short and prefer translucent SDR graphics to bright opaque content because some devices are prone to image retention. Show interactive overlays gracefully: implement a minimum delay of 0.5 seconds to pause media before displaying an interactive overlay (quizzes, surveys), with a clear way to dismiss and resume.
  - visionOS: help people stay comfortable (let them choose when to start, use a small resizable window, keep surroundings visible). In a fully immersive experience, avoid letting virtual content obscure playback or transport controls in the ornament near the bottom of the player. Avoid automatically starting a fully immersive video playback experience. Create a thumbnail track for scrubbing with thumbnails 160 px in width. Avoid expanding an inline video player to fill a window; inline video is 2D and window content should remain visible around it. Use a RealityKit video player for splash or transitional views that don't need controls.
  - watchOS: the system manages video; apps play short clips in the foreground, inline via a movie element or in a separate interface. Keep video clips short: no longer than 30 seconds. Use recommended encoding: H.264 High Profile; 160 kbps at up to 30 fps; full-screen resolution 208x260 px (portrait); 16:9 resolution 320x180 px (landscape); audio 64 kbps HE-AAC; avoid scaling clips. Avoid creating a poster image that looks like a system control. Consider a poster image that represents the clip's contents.
  - No additional considerations for iOS, iPadOS, or macOS.
- **Copy/labels:** Content tabs are named by purpose (Info, Episodes, Chapters). Don't prompt "Resume playback?"; just resume.
- **APIs:** AVKit (AVPlayerViewController, VideoPlayer), AVFoundation (`resizeAspectFill`, `resizeAspect`, `externalMetadata`), AVAudioSession `silenceSecondaryAudioHintNotification`, HTTP Live Streaming (Trick Play), RealityKit, Ornaments.
- **Web translation:** Use the native `video` element with native controls, preserve the source aspect ratio with `object-fit`, support Space and Media Session keys, resume at the last position without asking, and show a plain dark loading state with a spinner only when startup exceeds about two seconds. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/playing-video.md)

### Printing
- **Summary:** An iOS, iPadOS, macOS, or visionOS app can integrate system-provided print functionality when it makes sense, presenting custom printer- and document-specific options if necessary.
- **Platforms:** ios, ipados, macos, visionos
- **When this applies:**
  - Any content that people might print (documents, tickets, receipts, images).
  - Placing and enabling the Print action; presenting print options.
  - macOS apps with app-specific print settings or page setup.
- **Rules:**
  - Make printing discoverable: a Print item in the macOS File menu; in iOS and iPadOS a toolbar button that opens an action sheet; optionally a customizable toolbar button in macOS.
  - Present a printing option only when it's possible: dim the Print menu item in macOS and remove the Print action from the action sheet in iOS and iPadOS when there's nothing to print or no printers are available; dim or hide a custom print button.
  - Present relevant printing options (page range, copies, two-sided) using the system-provided view when the printer supports them.
- **Platform notes:**
  - macOS: if your app offers app-specific print options the system doesn't, consider creating a custom category for the print panel with a unique name such as your app name (Keynote offers presenter notes, slide backgrounds, skipped slides). If you support document-specific page settings, consider a page setup dialog (page size, orientation, scaling) without duplicating system options like reverse order. Make interdependencies between options clear (transparencies unavailable when double-sided is on). Separate advanced features from frequently used ones with a disclosure control and label them "Advanced Options". Consider letting people preview the effect of a setting (thumbnail). Consider storing modified settings with the document, at minimum until it closes.
  - No additional considerations for iOS, iPadOS, or visionOS. Not supported in tvOS or watchOS.
- **Copy/labels:** Menu item "Print"; advanced section labeled "Advanced Options"; custom print panel category named for your app.
- **APIs:** UIPrintInteractionController (UIKit), NSDocument (AppKit).
- **Web translation:** Offer a Print action only when printable content exists, call `window.print()` and rely on the browser's dialog, and supply a print stylesheet instead of custom print UI. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/printing.md)

### Ratings and reviews
- **Summary:** People often view the ratings and reviews for an app or game before they download it.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Deciding when and how often to ask for an App Store rating.
  - Using the system rating prompt versus any custom prompt.
  - Releasing a new version and considering a rating reset.
- **Rules:**
  - Ask for a rating only after people have demonstrated engagement (completing a level or a significant task); avoid asking on first launch or during onboarding.
  - Avoid interrupting people while they're performing a task or playing a game; use natural breaks or stopping points.
  - Avoid pestering people; consider allowing at least a week or two between requests, prompting again only after additional engagement.
  - Prefer the system-provided prompt (iOS, iPadOS, macOS): it asks for a rating and optional review, can be dismissed with a single tap or click, and people can opt out for all apps. The system automatically limits the prompt to three occurrences per app within a 365-day period.
  - Weigh the benefits of resetting your summary rating against the potential disadvantage of showing fewer ratings when you release a new version.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Use the system prompt's wording; don't build a custom rating dialog.
- **APIs:** RequestReviewAction (StoreKit), App Store Connect reset app summary rating.
- **Web translation:** Ask for feedback or a store review only after a completed meaningful task, at a natural pause, no more than a few times per year, with a one-click dismiss. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/ratings-and-reviews.md)

### Searching
- **Summary:** People use various search techniques to find content on their device, within an app, and within a document or file.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any search field, search tab, or find-in-document feature.
  - Search suggestions, recent searches, scopes, and filters.
  - Making app content discoverable in Spotlight.
- **Rules:**
  - If search is important, give it a primary position in your app or view (Notes puts it in the bottom toolbar; Photos and Apple TV use a dedicated Search tab).
  - Aim to make your app's content searchable through a single location; a local search can still be useful for distinct sections (Music filters the current view).
  - Clearly display the current scope of a search with descriptive placeholder text, a scope bar, or a title (Mail always shows which mailbox is searched).
  - Provide suggestions to make searching easier: recent searches before typing and predictive suggestions while typing.
  - Take privacy into consideration before displaying search history; if you show it, provide a way to clear it.
  - Systemwide search: make your app's content searchable in Spotlight by making it indexable with descriptive metadata.
  - Define metadata for custom file types you handle with a Spotlight File Importer plug-in (CSImportExtension).
  - Use Spotlight to offer advanced file-search capabilities within your app (a button that starts a Spotlight search for the current selection).
  - Prefer using the system-provided open and save views, which include a built-in search field.
  - Implement a Quick Look generator if your app produces custom file types so Spotlight and other apps show previews.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Placeholder text names the scope (for example the mailbox or section being searched).
- **APIs:** `searchSuggestions(_:)` (SwiftUI), Core Spotlight (Adding your app's content to Spotlight indexes, CSImportExtension), Quick Look, Search fields and Scope bars and tokens components.
- **Web translation:** Put one site-wide search in the header, show recent and suggested queries with a Clear option, label the scope in the placeholder or a filter chip, and expose structured metadata so external search engines can index content. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/searching.md)

### Settings
- **Summary:** People expect apps and games to just work, but they also appreciate having ways to customize the experience to fit their needs.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Deciding which options belong in an in-app settings area, in the task itself, or in the system Settings app.
  - Building a macOS settings window.
  - Default values and respecting systemwide settings.
- **Rules:**
  - Aim to provide default settings that give the best experience to the largest number of people (auto-maximize game performance for the device instead of asking).
  - Minimize the number of settings you offer.
  - Make settings available in ways people expect: Command-Comma (,) opens an app's settings with a keyboard; games often use Esc.
  - Avoid using settings to ask for setup information you can get in other ways (detect a connected controller; detect Dark Mode).
  - Respect people's systemwide settings and avoid including redundant versions of them (accessibility, scrolling, authentication).
  - General settings: put general, infrequently changed settings in your custom settings area (window configuration, game-saving behavior, keyboard mappings, account options).
  - Task-specific options: when possible, prefer letting people modify task-specific options without going to your settings area (show or hide parts of a view, reorder, filter) in the screens they affect. In games, players adjust approach as gameplay, not as settings.
  - System settings: add only the most rarely changed options to the system-provided Settings app; consider a button that opens it directly from your interface.
- **Platform notes:**
  - macOS: the Settings item in the App menu opens your settings window, typically with a toolbar of buttons that switch between panes. Include a settings item in the App menu; avoid settings buttons in a window toolbar; put document-level options in the File menu. Dim a settings window's minimize and maximize buttons. Use a noncustomizable toolbar that remains visible and always indicates the active toolbar button. Update the window's title to reflect the currently visible pane; with a single pane, title it "App Name Settings". Restore the most recently viewed pane.
  - watchOS: apps don't add custom settings to the system Settings app; make a small number of essential options available at the bottom of the main view or via a More menu.
  - No additional considerations for iOS, iPadOS, tvOS, or visionOS.
- **Copy/labels:** macOS window title matches the current pane, or "App Name Settings" for a single pane; the menu item is "Settings" in the App menu; shortcut Command-Comma.
- **APIs:** Settings (SwiftUI), UserDefaults (Foundation), Preference Panes, Improving your game's graphics performance and settings (Metal).
- **Web translation:** Ship sensible defaults, keep view-specific toggles in the view, group rare preferences on one short settings page that remembers the last section, and honor OS-level preferences like `prefers-color-scheme` and `prefers-reduced-motion` instead of duplicating them. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/settings.md)

### Undo and redo
- **Summary:** Undo and redo gives people easy ways to reverse many types of actions, which can also help people explore and experiment safely as they learn a new interface or task.
- **Platforms:** ios, ipados, macos, visionos
- **When this applies:**
  - Any editing or content-manipulation experience (text, drawing, documents, lists).
  - Naming undo actions in menus and alerts.
  - Deciding whether to add dedicated undo and redo buttons.
- **Rules:**
  - Help people predict the results of undo and redo: describe the result in the shake alert on iPhone; modify menu item labels (Undo Typing, Redo Bold).
  - Show the results of an undo or redo; if the affected content is offscreen, scroll to reveal it so people don't repeat the action.
  - Let people undo multiple times; people expect to undo every action since opening a document or saving.
  - Consider giving people the option to revert multiple changes at once (a batch of incremental adjustments, or everything since opening or saving).
  - Provide undo and redo buttons only when necessary; people expect the Edit menu, keyboard shortcuts, or shaking iPhone. If buttons are important, use the standard system symbols in a toolbar.
- **Platform notes:**
  - iOS, iPadOS: avoid redefining standard gestures for undo and redo (three-finger swipe, shake). Briefly and precisely describe the operation to be undone or redone; the alert title automatically prefixes "Undo " or "Redo " (with trailing space), so you supply a word or two, for example "Undo Name" or "Redo Address Change".
  - macOS: place undo and redo commands at the top of the Edit menu and support Command-Z and Shift-Command-Z.
  - No additional considerations for visionOS. Not supported in tvOS or watchOS.
- **Copy/labels:** Menu labels "Undo Typing", "Redo Bold"; iOS alert titles like "Undo Name" or "Redo Address Change" (supply only the words after the automatic "Undo " or "Redo " prefix).
- **APIs:** UndoManager (Foundation), Edit menu, Standard keyboard shortcuts.
- **Web translation:** Support Ctrl/Cmd-Z and Shift-Ctrl/Cmd-Z globally with an unbounded history, name the action in the Edit menu or toast ("Undo Delete"), scroll to and highlight the restored content, and offer "Revert to saved" for bulk reversal. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/undo-and-redo.md)

### Workouts
- **Summary:** A great workout or fitness experience encourages people to engage with their current activity and helps them track their progress on their devices.
- **Platforms:** ios, ipados, watchos
- **When this applies:**
  - Fitness apps with active workout sessions on Apple Watch, iPhone, or iPad.
  - Displaying metrics during motion, controls to pause, resume, and end, and the end-of-session summary.
  - Using Activity rings.
- **Rules:**
  - In a watchOS fitness app, use workout sessions to provide useful data and relevant controls; watchOS keeps the app displayed between wrist raises, so show elapsed or remaining time, calories, distance, and controls like lap or interval markers.
  - Avoid distracting people from a workout with information that's not relevant (no workout lists or other app areas mid-session). Common arrangement: large session controls (End, Resume, New) on the leftmost screen, glanceable metrics on a dedicated screen, media playback controls on the rightmost screen.
  - Use a distinct visual appearance to indicate an active workout (real-time updating metrics, a unique layout).
  - Provide workout controls that are easy to find and tap (pause, resume, stop) with clear feedback when a session starts or stops.
  - Help people understand the health information your app records if sensor data is unavailable (water blocking heart rate during a swim); for Swimming or Other workout types, use language similar to the Workout app, for example "GPS is not used during a Pool Swim, and water may prevent a heart-rate measurement, but Apple Watch will still track your calories, laps, and distance using the built-in accelerometer." and "In this type of workout, you earn the calorie equivalent of a brisk walk anytime sensor readings are unavailable."
  - Provide a summary at the end of a session that confirms completion and shows recorded information; consider including Activity rings.
  - Discard extremely brief workout sessions (ending a few seconds after starting): discard automatically or ask whether to record.
  - Make sure text is legible for when people are in motion: large fonts, high contrast, most important information easiest to read.
  - Use Activity rings correctly: only for their documented purpose, with colors and meanings matching the Activity app.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, or watchOS. Not supported in macOS, tvOS, or visionOS.
- **Copy/labels:** Control labels End, Resume, New; sensor-unavailability explanations modeled on the Workout app text quoted above.
- **APIs:** WorkoutKit, HealthKit Workouts and activity rings, Activity rings component, Live Activities and Siri (iOS workout tracking).
- **Web translation:** For a web fitness tracker, show a dedicated high-contrast large-type metrics view during a session, keep Start, Pause, and End as big persistent controls, show a summary on completion, and discard sessions of only a few seconds. (Translation, not Apple guidance.)
- **Source:** [reference](../references/patterns/workouts.md)

## Inputs

### Action button
- **Summary:** The Action button gives people quick access to their favorite features on supported iPhone and Apple Watch models.
- **Platforms:** ios, watchos
- **When this applies:**
  - Apps that offer App Shortcuts that people can assign to the Action button.
  - Apple Watch Ultra apps for workouts, dives, or waypoints that use first and subsequent presses.
  - Writing the labels that appear in Settings when people configure the button.
- **Rules:**
  - Support the Action button with a set of your app's essential functions (a "Start Egg Timer" action in a cooking app); you don't need a shortcut that opens your app because the system already provides it.
  - For each action you support, write a short label that succinctly describes it: title-style capitalization, begins with a verb, present tense, no articles or prepositions, maximum of three words ("Start Race", not "Started Race" or "Start the Race").
  - Prefer letting the system show people how to use the Action button with your app; don't repeat the Settings guidance or system usage tips.
- **Platform notes:**
  - iOS: let people use your actions without leaving their current context, using Live Activities and custom snippets ("Set Timer" prompts for a duration and starts a Live Activity without opening Clock).
  - watchOS: first press can drop a waypoint, start a dive, or begin a specific workout; subsequent presses support secondary actions like marking a segment or moving to the next modality. Consider offering a secondary function that supports or advances the primary action, learnable without looking; be cautious about more than one secondary function. Prefer using subsequent button presses to support additional functionality rather than to stop or conclude a function; put stop in your interface. Pause the current function when people press the Action button and side button together, except in a diving app where pausing could be dangerous.
  - Not supported in iPadOS, macOS, tvOS, or visionOS.
- **Copy/labels:** Verb-first, present tense, title case, no articles or prepositions, three words maximum (for example "Start Race").
- **APIs:** App Shortcuts, Live Activities, Workouts pattern, Digital Crown.
- **Web translation:** n/a (hardware button). A loose analogue is exposing your most-used actions as PWA shortcuts with verb-first labels of three words or fewer. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/action-button.md)

### Apple Pencil and Scribble
- **Summary:** Apple Pencil helps make drawing, handwriting, and marking effortless and natural, in addition to performing well as a pointer and UI interaction tool.
- **Platforms:** ipados
- **When this applies:**
  - iPad apps that support drawing, handwriting, annotation, or markup, and any iPad app with text fields (Scribble is on by default).
  - Responding to hover, double tap, squeeze, and barrel roll on supported Apple Pencil models.
  - Building a custom canvas with PencilKit.
- **Rules:**
  - Support behaviors people intuitively expect when using a marking instrument (writing in margins).
  - Let people choose when to switch between Apple Pencil and finger input; controls must respond to Apple Pencil too, or they seem broken. (Scribble only supports Apple Pencil input.)
  - Let people make a mark the moment Apple Pencil touches the screen; no button or special mode first.
  - Help people express themselves by responding to the way they use Apple Pencil: tilt (altitude), force (pressure), orientation (azimuth), and barrel roll; keep pressure mapping simple (opacity or brush size).
  - Provide visual feedback to indicate a direct connection with content; don't let the pencil appear to trigger disconnected actions elsewhere on screen.
  - Design a great left- and right-handed experience; avoid controls that a hand may obscure, or let people reposition them.
  - Hover: use hover to help people predict what will happen when Apple Pencil touches the screen (preview mark size and color); avoid continuously modifying the preview with height.
  - Avoid using hover to initiate an action, especially a destructive one.
  - Prefer showing a preview value that's near the middle in a range of dynamic values (not maximum or minimum pressure).
  - Consider using hover to support relevant interactions close to where people are marking (a contextual menu of tool sizes on squeeze or a modifier key).
  - Prefer showing hover previews for Apple Pencil, not for a pointing device.
  - Double tap: respect people's settings for the double-tap gesture when they make sense in your app (default toggles current tool and eraser; options include current and previous tool, show or hide color picker, or nothing); if they don't fit, you may use it to change interaction mode (a 3D app toggling raise and lower).
  - Give people a way to specify custom double-tap behavior if necessary, make it discoverable, and don't turn it on by default.
  - Avoid using the double-tap gesture to perform an action that modifies content; prefer easily undoable actions and avoid destructive ones.
  - Squeeze (Apple Pencil Pro): people may configure squeeze to run an App Shortcut instead; it works only when the iPad screen is on and the pencil isn't touching it. Treat squeeze as a single, quick gesture that performs a discrete, not continuous, action. If you use squeeze to reveal app UI like a contextual menu, display it close to Apple Pencil Pro. Define squeeze actions that are nondestructive and easy to undo.
  - Barrel roll (Apple Pencil Pro): use barrel roll only to modify marking behavior (rotate the angle of a highlighter), not to enable navigation or display other controls.
  - Scribble: make text entry feel fluid and effortless; Scribble works in all standard text components except password fields; custom text fields must not require a tap or selection before writing.
  - Make Scribble available everywhere people might want to enter text (Reminders lets people write in the blank space below the last item via UIIndirectScribbleInteraction).
  - Avoid distracting people while they write: avoid autocompletion text while writing and hide placeholder text the moment people begin to write.
  - While people are writing in a text field, make sure it remains stationary; delay moves or resizes until they pause.
  - Prevent autoscrolling text while people are writing and editing in a text field.
  - Give people enough space to write; increase the field size before writing starts or when they pause, never while writing (UIScribbleInteraction).
  - Custom drawing (PencilKit): help people draw on top of existing content by preventing the dynamic Dark Mode color adjustment when drawing over a PDF or photo.
  - Consider displaying custom undo and redo buttons when your app runs in a compact environment (the tool picker lacks them there); also consider supporting the standard 3-finger undo and redo gesture.
- **Platform notes:**
  - Not supported in iOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** n/a
- **APIs:** PencilKit, PaperKit, UIScribbleInteraction, UIIndirectScribbleInteraction, Adopting hover support for Apple Pencil (UIKit), App Shortcuts.
- **Web translation:** Use Pointer Events with `pointerType === "pen"`, read pressure and tilt to vary strokes, start marking on `pointerdown` with no mode switch, keep text fields stationary and free of autocomplete while a pen is writing, and never use hover alone to trigger actions. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/apple-pencil-and-scribble.md)

### Camera Control
- **Summary:** The Camera Control provides direct access to your app's camera experience.
- **Platforms:** ios
- **When this applies:**
  - Camera apps on iPhone 16 and iPhone 16 Pro models that expose controls in the Camera Control overlay.
  - Designing slider and picker controls, their symbols, labels, and prominent values.
  - Laying out the viewfinder around the overlay and supporting launch from a locked device.
- **Rules:**
  - Anatomy: a slider provides a range of values (contrast); a picker offers discrete options (grid on or off). The system also provides standard zoom factor and exposure bias controls you can include. A light press shows the overlay; a light double press shows available controls; sliding adjusts a value.
  - Use SF Symbols to represent control functionality; custom symbols aren't supported; symbols don't represent current state (see the Camera & Photos section of the SF Symbols app, for example `bolt.fill`, `camera.filters`).
  - Keep names of controls short; labels follow Dynamic Type and long names can obscure the viewfinder.
  - Include units or symbols with slider control values to provide context (EV, %, or a custom string via `localizedValueFormat`).
  - Define prominent values for a slider control (frequently chosen or evenly spaced values like major zoom increments) so the control lands on them easily.
  - Make space for the overlay in the viewfinder; the overlay and labels occupy the area adjacent to the Camera Control in portrait and landscape; place your UI outside those areas and maximize the viewfinder.
  - Minimize distractions in the viewfinder; avoid duplicating controls in your UI and the overlay when the overlay is displayed.
  - Enable or disable controls depending on the camera mode (disable video controls when taking photos); you can't add or remove controls at runtime.
  - Consider how to arrange your controls: common ones toward the middle, lesser used on either side; the system remembers the last control used in your app.
  - Allow people to use the Camera Control to launch your experience from anywhere via a locked camera capture extension (locked device, Home Screen, or within other apps).
- **Platform notes:**
  - Not supported in iPadOS, macOS, watchOS, tvOS, or visionOS.
- **Copy/labels:** Short control names; slider values carry units such as EV or %.
- **APIs:** AVCaptureControl, AVCaptureSlider (`localizedValueFormat`, `prominentValues`), Enhancing your app experience with the Camera Control (AVFoundation), LockedCameraCapture, SF Symbols.
- **Web translation:** n/a (hardware control).
- **Source:** [reference](../references/inputs/camera-control.md)

### Digital Crown
- **Summary:** The Digital Crown is an important hardware input for Apple Vision Pro and Apple Watch.
- **Platforms:** visionos, watchos
- **When this applies:**
  - watchOS apps: navigation between tabs and through lists, scrolling, pickers, and inspecting data.
  - Deciding on Digital Crown haptic detents.
  - visionOS: understanding that the system reserves the crown (volume, immersion, recenter, Accessibility, Home) and apps don't receive its data.
- **Rules:**
  - On Apple Vision Pro the crown adjusts volume, adjusts immersion in a portal, Environment, or Full Space app, recenters content, opens Accessibility settings, and exits to the Home View; apps don't receive direct crown information.
  - On Apple Watch (watchOS 10 and later) the crown is the primary input for navigation: Smart Stack widgets on the watch face, vertical movement on the Home Screen, switching vertically paginated tabs, scrolling lists and variable height pages. Apps don't respond to presses, which the system reserves.
  - Anchor your app's navigation to the Digital Crown: vertically oriented list, tab, and scroll views; back every crown interaction with a corresponding touch interaction.
  - Consider using the Digital Crown to inspect data in contexts where navigation isn't necessary (World Clock advances the time of day).
  - Provide visual feedback in response to Digital Crown interactions; if you track turns directly, update the interface programmatically.
  - Update your interface to match the speed with which people turn the Digital Crown; avoid updating so fast that values are hard to select.
  - Use the default haptic feedback when it makes sense; turn off detents if they don't match your animation; for tables with rows of very different heights, consider linear detents instead of row-based detents.
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, or tvOS.
- **Copy/labels:** n/a
- **APIs:** WKCrownDelegate (WatchKit), Immersive experiences (visionOS).
- **Web translation:** n/a (hardware input). For a wearable web view, ensure vertical scrolling and vertically stacked navigation. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/digital-crown.md)

### Eyes
- **Summary:** In visionOS, people look at a virtual object to identify it as a target they can interact with.
- **Platforms:** visionos
- **When this applies:**
  - Every interactive element in a visionOS app (system hover effect, custom hover effects).
  - Spacing, shape, and placement of targets so people can look at them comfortably.
  - Custom components made of multiple elements that need a single highlight region.
- **Rules:**
  - visionOS highlights what people look at (the hover effect) to show an indirect gesture like tap will work; the system may expand components on look (tab bar labels, tooltips). For privacy, visionOS doesn't tell apps where people look before they tap.
  - Always give people multiple ways to interact with your app and support accessibility features.
  - Design for visual comfort: keep needed objects within the field of view; avoid requiring multiple quick eye adjustments over a large area or across depth levels.
  - Place content at a comfortable viewing distance: aim to place content people read or engage with over time at least one meter away; don't put content very close unless it's brief.
  - Prefer using standard UI components, which respond consistently to looking.
  - Minimize visual distractions; movement in peripheral vision pulls the eyes (don't reveal content near a button people are looking at).
  - Make it easy for people to look at an item by providing enough space around it: a margin of at least 16 points around each interactive item's bounds, or centers at least 60 points apart.
  - Avoid using a repeating pattern or texture that fills the field of view (eyes can lock onto elements and perceive false depth); use the pattern in a smaller area.
  - Consider using subtle visual cues to encourage people to look at the item they're most likely to want (center of view, gentle motion, contrast, color, scale); noticeable but not flashy.
  - In general, give an interactive item a rounded shape; eyes drift to corners, so rounder shapes are easier to target.
  - If you create an interactive component that consists of more than one element, provide an overall containing shape that visionOS can highlight.
  - Custom hover effects: define two states (with and without the effect); the system applies it out of process so your code never knows when people are looking (a favorite symbol can be shown, but the favoriting action can't be triggered by looking).
  - Prefer using a custom hover effect to emphasize or enhance a special moment; too many dilute impact and cause discomfort.
  - Choose the right delay: no delay (default) for subtle effects that invite interaction like a slider knob; short delay to let people look and interact quickly (tab bar expansion); long delay for additional information like a tooltip.
  - Aim to keep one or more of the element's primary views unchanged in both states of a custom hover effect for visual stability.
  - Thoroughly test custom hover effects while wearing Apple Vision Pro.
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.
- **Copy/labels:** n/a
- **APIs:** Adopting best practices for privacy and user preferences (visionOS), RealityKit entities with hover effects, SwiftUI hover effect APIs referenced via Gestures and Spatial layout.
- **Web translation:** n/a for eye tracking. The spacing and rounded-target advice maps to generous hit areas and clear `:focus-visible` and `:hover` states. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/eyes.md)

### Focus and selection
- **Summary:** Focus helps people visually confirm the object that their interaction targets.
- **Platforms:** ipados, macos, tvos, visionos
- **When this applies:**
  - Keyboard, remote, or game controller navigation through UI (tvOS always; iPadOS and macOS with keyboards; visionOS with connected devices).
  - Custom views that must participate in the focus system, custom halo shapes, focus groups, and priorities.
  - tvOS layouts that must accommodate five focus states.
- **Rules:**
  - Focusing often selects, except when automatic selection would cause a distracting context shift (tvOS requires a separate select gesture).
  - Rely on system-provided focus effects; create custom ones only if absolutely necessary.
  - Avoid changing focus without people's interaction; the exception is when a focused item disappears while people use a discrete directional device (keyboard, remote, controller), in which case move focus to a nearby item; otherwise hide the focus indicator.
  - Be consistent with the platform: in iPadOS and macOS, Full Keyboard Access reaches controls, so support focus only for content elements (list items, text fields, search fields), not for buttons, sliders, and toggles; in tvOS every element must be focusable.
  - Indicate focus using visual appearances that are consistent with the platform (iPadOS and macOS focused list items use white text on an accent-color highlight; unfocused use standard text on a gray highlight).
  - In general, use a focus ring for a text or search field, but use a highlight in a list or collection (a ring is fine for an item that fills a cell, like a photo).
- **Platform notes:**
  - iPadOS: the focus system (iPadOS 15 and later) uses focus groups (sidebar, grid, list). Tab moves among focus groups; arrow keys move within a group. The halo effect (focus ring) outlines a component and applies to custom views and opaque cell content like images; customize the halo when necessary to match rounded corners or Bézier paths, and adjust its position if clipped or occluded. The highlighted appearance (text in accent color) indicates focus but isn't a focus effect. Ensure that focus moves through your custom views in ways that make sense (reading order: leading to trailing, top to bottom; mark a vertical stack as one focus group). Adjust the priority of an item to reflect its importance within a focus group so the primary item receives focus first.
  - tvOS: in a full-screen experience, let people use gestures to interact with the content, not to move focus. Avoid displaying a pointer; use the focus model for menus and interface elements; if a game needs a pointer, make it highly visible. Design your interface to accommodate components in various focus states: up to five states (unfocused, focused with elevation and scale, highlighted on choose, selected, unavailable); supply assets for the larger focused size and make sure it doesn't crowd neighbors.
  - visionOS: same focus system as iPadOS and tvOS for connected keyboards or controllers; looking at an object uses the hover effect, not a focus effect.
  - Not supported in iOS or watchOS.
- **Copy/labels:** n/a
- **APIs:** UIFocusHaloEffect, `focusGroupIdentifier`, UIFocusGroupPriority, UICollectionView and UICollectionViewCell (UIKit), NSTableView (AppKit), Focus-based navigation, About focus interactions for Apple TV, TVML Focus Attributes.
- **Web translation:** Never move focus programmatically except when the focused element is removed, use a visible `:focus-visible` ring on text inputs and a row highlight in lists, keep Tab order in reading order, and make every control reachable with a keyboard or TV remote. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/focus-and-selection.md)

### Game controls
- **Summary:** Precise, intuitive game controls enhance gameplay and can increase a player's immersion in the game.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **When this applies:**
  - Any game: touch controls on iPhone and iPad, physical controllers on all platforms except watchOS, keyboards on Mac and iPad.
  - Mapping controller buttons for menu navigation outside gameplay.
  - Spatial game controllers in visionOS.
- **Rules:**
  - Support both physical controllers and the platform's default interaction (touch, remote, mouse and keyboard, eyes and hands); not every player has a controller.
  - Touch controls: determine whether it makes sense to display virtual controls on top of game content; prefer direct interaction with in-game objects (tap to select) where possible.
  - Place virtual buttons where they're easy to access, respecting safe areas, the Home indicator, and the Dynamic Island; frequent buttons near the thumb, outside the regions used for movement and camera; secondary controls like menus at the top.
  - Make sure controls are large enough: frequently used controls a minimum size of 44x44 pt; less important controls such as menus a minimum of 28x28 pt.
  - Always include visible and tactile press states (a glow visible under the finger) combined with sound and haptics.
  - Use symbols that communicate the actions they perform (a weapon for attack); avoid abstract shapes or controller names like A, X, or R1.
  - Show and hide virtual controls to reflect gameplay (hide movement controls until the player touches the screen; fade a resting thumbstick).
  - Combine functionality into a single control (double tap and touch and hold variants; walk and sprint in one control) instead of simultaneous or sequential multi-button presses.
  - Map movement and camera controls to predictable behavior: movement on the left, camera on the right; show the thumbstick where the thumb lands; pan the camera with direct touch rather than a virtual stick; use as large an input area as possible.
  - Physical controllers: support the platform's default interaction method as a fallback.
  - Tell people about game controller requirements; tvOS and visionOS can require a controller (App Store shows a "Game Controller Required" badge); check for presence and gracefully prompt to connect one.
  - Automatically detect whether a controller is paired and read its profile.
  - Customize onscreen content to match the connected game controller's labeling scheme.
  - Map controller buttons to expected UI behavior outside gameplay: A activates a control; B cancels or returns to the previous screen; Left shoulder navigates left to a different screen or section; Right shoulder navigates right; thumbsticks and directional pad move selection; Home or logo is reserved for the system; Menu opens game settings or pauses gameplay; X, Y, and triggers have no assigned UI behavior.
  - Support multiple connected controllers, using labels and glyphs that match the controller the player is actively using.
  - Prefer using symbols, not text, to refer to game controller elements (SF Symbols cover buttons on various controller brands).
  - Keyboards: prioritize single-key commands (I for Inventory, M for Map, Space for the main action).
  - Test key binding comfort using an Apple keyboard; consider remapping Control to Command, which sits next to Space near W, A, S, D.
  - Take the proximity of keys into account (nearby keys for high-value commands; number keys for inventory categories).
  - Let players customize key bindings.
- **Platform notes:**
  - visionOS: match spatial game controller behavior (such as PlayStation VR2 Sense controller) to hand input; support looking at an object and pressing a trigger to interact indirectly, or reaching out and pressing a trigger to interact directly.
  - No additional considerations for iOS, iPadOS, macOS, or tvOS. Not supported in watchOS.
- **Copy/labels:** Button artwork depicts the action, not A, X, or R1; refer to controller elements with the connected controller's own glyphs via SF Symbols rather than text.
- **APIs:** Touch Controller framework, Game Controller framework (GCControllerElement, GCRequiresControllerUserInteraction), Adding virtual controls to games that support game controllers in iOS, SF Symbols, Metal.
- **Web translation:** Use the Gamepad API with the standard mapping (button 0 activates, button 1 cancels), keep touch controls at least 44 CSS px with visible pressed states, allow key remapping, and always provide a touch or keyboard fallback. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/game-controls.md)

### Gestures
- **Summary:** A gesture is a physical motion that a person uses to directly affect an object in an app or game on their device.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Every touch, trackpad, remote, or hand interaction; standard gestures must behave as expected everywhere.
  - Adding custom or shortcut gestures.
  - Avoiding conflicts with system gestures (edge swipes, visionOS palm overlays, watchOS double tap).
- **Rules:**
  - Give people more than one way to interact with your app (voice, keyboard, Switch Control); don't assume a specific gesture is possible.
  - In general, respond to gestures in ways that are consistent with people's expectations (tap activates or selects); don't repurpose tap or swipe for app-unique actions or invent gestures for standard actions.
  - Handle gestures as responsively as possible, with feedback that predicts the result and communicates the movement required.
  - Indicate when a gesture isn't available (locked object, unavailable button) so people don't think the app froze.
  - Add custom gestures only when necessary, for frequent specialized tasks (games, drawing); make them discoverable, straightforward to perform, distinct from other gestures, and never the only way to perform an important action.
  - Make custom gestures easy to learn, teach them in context, and test in real use; if it's hard to describe simply, it's hard to perform.
  - Use shortcut gestures to supplement standard gestures, not replace them (keep the Back button even with an edge swipe).
  - Avoid conflicting with gestures that access system UI (watchOS edge swipe, visionOS hand roll); in games or immersive experiences you may defer the system gesture.
  - Standard gestures (all platforms unless noted): Tap activates a control or selects an item; Swipe reveals actions and controls, dismisses views, scrolls; Drag moves a UI element; Touch (or pinch) and hold reveals additional controls; Double tap zooms in or out, opens an item on a Mac with a touch display, performs a primary action on Apple Watch Series 9 and later and Apple Watch Ultra 2 and later; Zoom and Rotate (not watchOS).
- **Platform notes:**
  - iOS, iPadOS: additional gestures: three-finger swipe (undo left, redo right), three-finger pinch (copy in, paste out), four-finger swipe (iPadOS only, switch apps), shake (undo or redo). Consider allowing simultaneous recognition of multiple gestures in games (joystick plus fire buttons).
  - macOS: keyboard and pointing device are primary; touch is a secondary input on a Mac with a touch display or an iPad via Sidecar. Keep the layout and size of interface elements the same when you support touch. Make tap targets bigger, not the controls themselves. Consider providing expandable controls (temporary touch-sized variants that persist briefly after lift; steppers, sliders, and dials do this automatically). Don't use touch as the only way to access controls or features, and provide touch equivalents for pointer-only actions. Where possible, align with gestures people already know from iPhone, iPad, or trackpad. Make sure custom gestures work for both touch and trackpad, using modifier keys where needed. Trackpad versus touch display: select is primary click or tap; open is double click or double tap; scroll is two-finger slide or one-finger slide; zoom is pinch on both; rotate is two fingers around each other on both; context menu is secondary click or touch and hold; drag is click and drag or touch and hold then drag.
  - tvOS: standard gestures on the Siri Remote or a controller with a touch surface; see Remotes.
  - visionOS: indirect gestures (look, then pinch at a distance) and direct gestures (touch virtual objects). Direct gestures: Touch selects or activates; Touch and hold opens a contextual menu; Touch and drag moves; Double touch previews or selects a word; Swipe reveals, dismisses, scrolls; two-hand pinch and drag apart or together zooms; two-hand pinch and drag in a circle rotates. Support standard gestures everywhere you can. Offer both indirect and direct interactions when possible; prefer indirect for UI and buttons, reserve direct and custom for close-up objects and games. Avoid requiring specific body movements or positions for input. Custom gestures require a Full Space and permission for hand data: prioritize comfort (arms raised quickly tire), carefully consider complex gestures involving multiple fingers or both hands and offer alternatives, avoid custom gestures that require a specific hand. System overlays (visionOS 2): looking at the palm reveals Home; turning the hand reveals the status bar and Control Center; reserve the area around a person's hand for system overlays and don't anchor content to hands or wrists; consider deferring the system overlay behavior in an immersive Full Space app (require a tap to reveal Home); use caution with custom gestures that involve a rolling motion of the hand, wrist, and forearm. visionOS 1 apps defer the overlay by default.
  - watchOS: double tap (watchOS 11 and later) scrolls lists and scroll views and advances vertical tabs; you can designate a toggle or button as the primary action in a view, widget, or Live Activity in the Smart Stack, and it acts on the first nondestructive notification action. Avoid setting a primary action in views with lists, scroll views, or vertical tabs. Choose the button that people use most commonly as the primary action (play/pause in media controls).
- **Copy/labels:** n/a
- **APIs:** SwiftUI Gestures, UITouch (UIKit), Adopting gesture recognizers in your app and Handling AppKit gestures (AppKit), `persistentSystemOverlays(_:)`, `handGestureShortcut(_:isEnabled:)` and `primaryAction` (SwiftUI), Setting up access to ARKit data.
- **Web translation:** Use Pointer Events for tap, drag, pinch, and rotate with native scroll untouched, never make a custom gesture the only path to a feature, keep edge regions free for browser and OS gestures, and show disabled states clearly so a failed gesture isn't mistaken for a hang. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/gestures.md)

### Gyroscope and accelerometer
- **Summary:** On-device gyroscopes and accelerometers can supply data about a device's movement in the physical world.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Fitness and health features that measure activity, and games that use motion.
  - Any access to motion data, which requires a permission string.
  - Considering motion gestures for navigating the interface (generally avoid).
- **Rules:**
  - Use motion data only to offer a tangible benefit to people (fitness feedback, gameplay); avoid gathering data simply to have it.
  - You must provide copy that explains why your experience needs motion data; the system includes it in the permission request the first time you access the data.
  - Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface; motion gestures are hard to replicate precisely, may be physically challenging, and affect battery.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS. (tvOS apps can use gyroscope data from the Siri Remote; iOS, iPadOS, and watchOS apps use device motion.)
- **Copy/labels:** Write a purpose string explaining why motion data is needed; it appears in the system permission request.
- **APIs:** Core Motion (Getting processed device-motion data), HealthKit walking metrics referenced in the video.
- **Web translation:** Request `DeviceMotionEvent` permission only on a user action with an explanation of the benefit, use motion for games or fitness only, and never make tilt or shake the sole way to navigate. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/gyro-and-accelerometer.md)

### Keyboards
- **Summary:** A physical keyboard can be an essential input device for entering text, playing games, controlling apps, and more.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **When this applies:**
  - Any app on a device that can connect a keyboard (all except Apple Watch); Mac always, iPad often.
  - Defining keyboard shortcuts, respecting standard ones, and supporting Full Keyboard Access.
  - Shortcut discoverability on iPad (hold Command) and Vision Pro.
- **Rules:**
  - A keyboard shortcut combines a primary key with modifiers (Control, Option, Shift, Command); a game's single-key shortcut is a key binding (see Game controls).
  - Support Full Keyboard Access when possible (iOS, iPadOS, macOS, visionOS); test by enabling it in Accessibility settings. In iPadOS, avoid supporting keyboard navigation for controls (buttons, segmented controls, switches); support it for text fields, text views, sidebars, and collection views, and let Full Keyboard Access handle controls and gestures like drag and drop.
  - Respect standard keyboard shortcuts; for a frequent unique action, create a custom shortcut rather than repurposing a standard one. Games should still honor shortcuts like Command-Q and let people modify key bindings.
  - In general, don't repurpose standard keyboard shortcuts for custom actions; redefine one only if its action doesn't make sense in your app (an app without text editing could use Command-I for Get Info).
  - Standard shortcuts people expect include: Command-Space Spotlight; Shift-Tab reverse navigation; Command-Tab app switching; Esc cancel; Command-Comma app settings; Command-Period cancel operation; Command-Question mark Help menu; Command-A select all; Command-B bold; Command-C copy; Command-F find; Control-Command-F enter full screen; Command-G find next; Command-H hide; Command-I italic or Info; Command-M minimize; Command-N new; Command-O open; Command-P print; Shift-Command-P page setup; Command-Q quit; Command-S save; Shift-Command-S duplicate or Save As; Option-Command-T toggle toolbar; Command-U underline; Command-V paste; Command-W close window; Command-X cut; Command-Z undo; Shift-Command-Z redo; Shift-Command-3 and 4 screenshots; Option-Command-D toggle Dock; Control-F1 through F7 move focus to menu bar, Dock, windows, toolbar, panels; arrow keys with Shift, Option, Control, and Command for selection extension and focus movement. Input-source shortcuts: Control-Space toggles input source; Control-Option-Space next input source. (Full table in the reference.)
  - Custom shortcuts: define custom keyboard shortcuts for only the most frequently used app-specific commands.
  - Use modifier keys in ways that people expect (Command-drag moves a group; Shift-drag constrains aspect ratio; holding an arrow key nudges by the smallest unit).
  - Modifier usage: prefer Command as the main modifier; prefer Shift as a secondary modifier complementing a related shortcut; use Option sparingly for less-common or power features; avoid Control, which the system uses widely. Some languages need modifiers to type characters (Option-5 is "{" on a French keyboard), so avoid extra modifiers with characters not on all keyboards; if you must, use them only with alphabetic characters.
  - List modifier keys in the correct order: Control, Option, Shift, Command.
  - Avoid adding Shift to a shortcut that uses the upper character of a two-character key (Help is Command-Question mark, not Shift-Command-Slash).
  - Let the system localize and mirror your keyboard shortcuts (right-to-left layouts).
  - Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command (Shift-Command-Z must stay related to undo and redo).
- **Platform notes:**
  - visionOS: shortcuts appear in the interface shown when people hold Command, organized by system-defined categories like File, Edit, and View, all in one view, listing only available commands with shortcuts. Write descriptive shortcut titles because submenu titles aren't shown (`discoverabilityTitle`). Recognize that people see a virtual keyboard overlay with completions when using a physical keyboard.
  - No additional considerations for iOS, iPadOS, macOS, or tvOS. Not supported in watchOS.
- **Copy/labels:** Shortcut titles should be descriptive on their own; display modifiers in the order Control, Option, Shift, Command; show the upper character (for example "?") rather than Shift plus the lower character.
- **APIs:** KeyboardShortcut and Input events (SwiftUI), Handling key presses made on a physical keyboard and UIKeyCommand `discoverabilityTitle` (UIKit), Mouse, Keyboard, and Trackpad and `isFullKeyboardAccessEnabled` (AppKit), Focus-based navigation.
- **Web translation:** Don't override browser or OS shortcuts (Cmd/Ctrl-T, W, N, F, Z), use Cmd/Ctrl as the primary modifier for a few frequent custom shortcuts, document them in a shortcut sheet, keep all functionality reachable by Tab plus Enter, and respect RTL mirroring. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/keyboards.md)

### Nearby interactions
- **Summary:** Nearby interactions support on-device experiences that integrate the presence of people and objects in the nearby environment.
- **Platforms:** ios, ipados, watchos
- **When this applies:**
  - Features based on distance and direction between devices with Ultra Wideband (U1 chip), such as handoff by proximity or finding an item.
  - Designing feedback that changes with proximity.
  - Onboarding that explains device orientation and obstructions.
- **Rules:**
  - People grant permission for their device to interact while using your app; the framework uses random, session-scoped identifiers to preserve privacy.
  - Consider a task from the perspective of the physical world to find inspiration for a nearby interaction (bring devices together to transfer a song).
  - Use distance, direction, and context to inform an interaction (share sheet suggesting the closest contact the person is facing).
  - Consider how changes in physical distance can guide a nearby interaction; perception sharpens as people get closer (AirTag finding moves from an arrow to a pulsing circle).
  - Provide continuous feedback that responds to people's movements.
  - Consider using multiple feedback types (visual while looking at the screen; audible and haptic while interacting with the environment).
  - Avoid using a nearby interaction as the only way to perform a task.
  - Device usage: encourage people to hold the device in portrait orientation, preferring implicit visual feedback over explicit instructions.
  - Design for the device's directional field of view (similar to the Ultra Wide camera on iPhone 11 and later); outside it you may get distance but not direction.
  - Help people understand how intervening objects (people, animals, large objects) can reduce accuracy; add advice to onboarding or tutorials.
- **Platform notes:**
  - iOS: APIs provide a peer device's distance and direction.
  - watchOS: APIs provide a peer device's distance only; all participating watchOS apps must be in the foreground.
  - No additional considerations for iPadOS. Not supported in macOS, tvOS, or visionOS.
- **Copy/labels:** Avoid explicitly telling people to hold the device in portrait; guide implicitly with visuals.
- **APIs:** Nearby Interaction framework.
- **Web translation:** n/a (no UWB access in browsers).
- **Source:** [reference](../references/inputs/nearby-interactions.md)

### Pointing devices
- **Summary:** People can use a pointing device like a trackpad or mouse to navigate the interface and initiate actions.
- **Platforms:** ios, ipados, macos, visionos
- **When this applies:**
  - Mac apps always; iPad and Vision Pro apps when a trackpad or mouse is attached.
  - Pointer shapes, content effects (highlight, lift, hover), accessories, hit regions, and custom pointer effects on iPadOS.
  - macOS cursors, trackpad gestures, and revealing hover-only controls with touch.
- **Rules:**
  - Be consistent when responding to mouse and trackpad gestures ("Swipe between pages" behaves the same across documents, webpages, and images).
  - Avoid redefining systemwide trackpad gestures (Dock, Mission Control), even in games; people can customize them.
  - Provide a consistent experience in your app whether people use gestures, eyes, a pointing device, or a keyboard.
  - Let people use the pointer to reveal and hide controls that automatically minimize or fade out (minimized Safari toolbar, full-screen playback controls).
  - Provide a consistent experience when people press and hold a modifier key while interacting (Option-drag duplicates whether by touch or pointer).
- **Platform notes:**
  - iPadOS: the pointer adapts to context and doesn't replace touch. Allow multiple selection in custom views when necessary (band selection via UIBandSelectionInteraction; standard nonlist collections support it). Distinguish between pointer and finger input only if it provides value (precise seek in a scrubber). Pointer shape defaults to an arrow and becomes an I-beam over text. Content effects: highlight materializes a Liquid Glass shape between pointer and control (default for bar buttons, tab bars, segmented controls, edit menus); lift scales the element with a shadow and specular highlight (default for standalone Liquid Glass controls, app icons, Control Center buttons); hover applies custom scale, tint, or shadow without changing the pointer shape. Pointer accessories indicate possible interactions (resize arrows): use clear, simple images, and consider the accessory transition to signal a state change (`plus` to `circle.slash`). When possible, support the system-provided content effects: highlight for a group of controls in a Liquid Glass container; lift for a standalone Liquid Glass control or small opaque element; hover for large elements. Prefer the system-provided pointer appearances for standard buttons and text-entry areas. Add padding around interactive elements to create comfortable hit regions: about 12 points around elements with a bezel and about 24 points around elements without a bezel. Create contiguous hit regions for custom bar buttons so the highlight doesn't flicker between buttons. Customizing: prefer system pointer effects for custom elements that behave like standard ones; use pointer effects consistently; avoid gratuitous pointer and content effects; keep custom pointer shapes simple; consider custom annotations with useful information (X and Y values, width and height); avoid displaying instructional text with a pointer; consider the interplay of shadow, scale, and spacing (don't scale table rows; don't use shadow without scale; use tint alone for tightly spaced elements).
  - macOS: standard mouse and trackpad behaviors people can customize: primary click selects or activates; secondary click reveals context menus; scrolling; smart zoom; swipe between pages; swipe between full-screen apps; Mission Control; lookup and data detectors (force click or three-finger tap, trackpad); tap to click; force click for Quick Look or pressure-sensitive controls; pinch zoom; rotate; Notification Center edge swipe; App Exposé; Apps (pinch thumb and three fingers); Show Desktop (spread thumb and three fingers). Standard pointers and meanings: arrow (default), closed hand (dragging), context menu (shown with Control), cross (precise rectangular selection), disappearing item (dragged item will vanish), drag copy (Option during drag), drag link (Option and Command during drag creates an alias), horizontal and vertical I-beam (text), open hand (draggable), operation not allowed, pointing hand (URL link), resize up, down, left, right, and the frame resize variants (east, west, north, south, and diagonals, with single-direction variants when a min or max is reached), zoom in, zoom out. Touch support for hidden controls (controls that appear only on pointer hover): decide which hidden controls need touch support (essential ones only; not tooltips or features already reachable by touch; don't keep hidden controls always visible). Reveal a hidden control when someone taps its general location, show only controls relevant to the content, and hide it when finished or after a few seconds. Retain the current selection when revealing a hidden control. Make essential hidden controls available in a context menu (touch and hold opens it). In a sidebar, reveal hidden controls when someone taps the corresponding section header or row, keep them visible until touch leaves the sidebar or a pointing device is used, and reveal without activating on a tap of the hidden area. In a tabbed window, reveal the selected tab's close button when someone taps anywhere in the window and keep it until a pointing device is used again.
  - visionOS: looking at an element then moving the pointer brings focus to it automatically; the pointer's context follows the window people look at; the pointer hides while gesturing on a trackpad or mouse and reappears where people are looking.
  - No additional considerations for iOS. Not supported in tvOS or watchOS.
- **Copy/labels:** Don't attach instructional text to the pointer; annotations show values (dimensions, coordinates) only.
- **APIs:** Pointer interactions, UIBandSelectionInteraction, UIPointerAccessory (UIKit), NSCursor (AppKit: arrow, closedHand, contextualMenu, crosshair, disappearingItem, dragCopy, dragLink, iBeam, openHand, operationNotAllowed, pointingHand, rowResize, columnResize, frameResize, zoomIn, zoomOut), SwiftUI PointerStyle (default, grabActive, grabIdle, rectSelection, horizontalText, verticalText, link, rowResize, columnResize, frameResize, zoomIn, zoomOut), Input events (SwiftUI), Mouse, Keyboard, and Trackpad (AppKit), Context menus.
- **Web translation:** Use semantic CSS cursors (`pointer` only for links, `grab`/`grabbing`, `text`, `not-allowed`, `col-resize`/`row-resize`), add roughly 12 to 24 px of padded hit area around small controls, show hover-only controls on tap for touch users and in a context menu, and keep hover effects subtle and consistent. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/pointing-devices.md)

### Remotes
- **Summary:** The Siri Remote is the primary input method for Apple TV, helping people feel connected to onscreen content from across the room.
- **Platforms:** tvos
- **When this applies:**
  - Every tvOS app and game: swipe and press on the clickpad touch surface, Back, and Play/Pause buttons.
  - Live-viewing apps responding to compatible remotes' guide, page up, and page down buttons.
  - Games that redefine button behavior during gameplay.
- **Rules:**
  - Prefer using standard gestures to perform standard actions; redefine them only during active gameplay.
  - Be consistent with the tvOS focus experience; always move focus in the same direction as the gesture.
  - Provide clear feedback that shows people what happens when they make gestures (resting a thumb shows where to swipe down for an info area).
  - Define new gestures only when it makes sense in your app (gameplay).
  - Differentiate between press and tap, and avoid responding to an inadvertent tap; pressing is intentional (choose, confirm, act); taps suit navigation or extra info, but avoid responding to taps during live video playback because resting a thumb or handing over the remote causes accidental taps.
  - Consider using the position of a tap (up, down, left, right) to aid navigation or gameplay, only if intuitive and discoverable.
  - In almost all cases, open the parent of the current screen when people press the Back button (the Home Screen at the top level; the app hierarchy's parent inside the app, not necessarily the previous screen). During active gameplay, respond to Back by opening an in-game pause menu; when the pause menu is open, Back closes it and resumes. Press and hold Back always goes Home.
  - Respond correctly to the Play/Pause button during media playback (play, pause, resume).
  - Gestures: swipe scrolls with momentum (edge swipes speed through items); press activates a control or selects an item, and pressing before swiping activates scrubbing mode.
  - Buttons table: touch surface swipe navigates and changes focus in an app, acts as a directional pad in a game; touch surface press activates or navigates deeper in an app, acts as the primary button in a game; Back returns to the previous screen or exits to Home in an app, pauses or resumes or exits to the main menu in a game; Play/Pause plays, pauses, or resumes media in an app, acts as the secondary button or skips an intro video in a game.
  - Compatible remotes: if your live-viewing app provides an EPG, respond to a remote's EPG-browsing buttons in ways people expect (a "guide" or "browse" button opens the EPG; "page up" and "page down" navigate it); don't respond to these buttons otherwise while browsing the EPG. Without an EPG, the system routes these presses to the default guide app.
  - While your content plays, respond to a compatible remote's "page up" or "page down" button by changing the channel.
- **Platform notes:**
  - Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.
- **Copy/labels:** n/a
- **APIs:** Providing Channel Navigation (TVServices), Focus and selection, Gestures, Live-viewing apps EPG experience.
- **Web translation:** For TV web apps, map arrow keys to focus movement, Enter to activate, Escape or Back to the parent view (pause menu during gameplay), Media Play/Pause keys to playback, and ignore accidental single taps during live video. (Translation, not Apple guidance.)
- **Source:** [reference](../references/inputs/remotes.md)
