# Technologies

This guide condenses every page in Apple's Human Interface Guidelines under **Technologies**: the Apple frameworks and services an app can integrate (payments, sign-in, Siri, maps, health, car, TV, AR, machine learning, generative AI, Wallet, Game Center, SharePlay, and more). Many of these pages carry strict requirements on button labels, trademark wording, logo usage, image sizes, and privacy, so faithfulness to Apple's text matters here even more than elsewhere.

Each entry keeps Apple's bold best-practice sentences as short imperative rules, preserves the exact numbers Apple gives, and calls out required wording under **Copy/labels**. Lines marked **Web translation** are this guide's own suggestion for honoring the same rule in a web app; they are not Apple guidance. Every entry links to the faithful copy of Apple's page under `../references/`.

## Technology by what the app wants to do

| The app wants to... | Technology entry |
|---|---|
| Sell physical goods, services, donations, or subscriptions billed through a card | [Apple Pay](#apple-pay) |
| Sell digital goods, premium features, or app subscriptions | [Apple In-App Purchase](#apple-in-app-purchase) |
| Accept contactless card payments as a merchant on iPhone | [Tap to Pay on iPhone](#tap-to-pay-on-iphone) |
| Store tickets, boarding passes, loyalty cards, IDs, or order tracking | [Wallet](#wallet) |
| Verify a customer's age or identity from a mobile ID in person | [ID Verifier](#id-verifier) |
| Offer sign-in or account creation | [Sign in with Apple](#sign-in-with-apple) |
| Expose actions and content to voice and Apple Intelligence | [Siri](#siri) |
| Show a map, place details, or indoor venue map | [Maps](#maps) |
| Read or write health and fitness data, show Activity rings | [HealthKit](#healthkit) |
| Build a care plan or patient app | [CareKit](#carekit) |
| Run a medical research study | [ResearchKit](#researchkit) |
| Control smart home accessories | [HomeKit](#homekit) |
| Run on the car display | [CarPlay](#carplay) |
| Stream media to TVs and speakers | [AirPlay](#airplay) |
| Place virtual objects in the real world | [Augmented reality](#augmented-reality) |
| Use models for recommendations, recognition, or prediction | [Machine learning](#machine-learning) |
| Generate or transform text, images, or other content with AI | [Generative AI](#generative-ai) |
| Recognize music or synchronize to audio | [ShazamKit](#shazamkit) |
| Add achievements, leaderboards, challenges, or multiplayer | [Game Center](#game-center) |
| Let people do an activity together over FaceTime | [SharePlay](#shareplay) |
| Sync documents, settings, and game saves across devices | [iCloud](#icloud) |
| Offer a lightweight, instant task or demo without installing the app | [App Clips](#app-clips) |
| Scan NFC tags on objects | [NFC](#nfc) |
| Extend Messages with an app or sticker pack | [iMessage apps and stickers](#imessage-apps-and-stickers) |
| Display or edit Live Photos | [Live Photos](#live-photos) |
| Add a photo editing extension to Photos | [Photo editing](#photo-editing) |
| Bring an iPad app to the Mac | [Mac Catalyst](#mac-catalyst) |
| Keep showing useful information when the display dims | [Always On](#always-on) |
| Support people who can't see the screen | [VoiceOver](#voiceover) |

### AirPlay
- **Summary:** AirPlay lets people stream media content wirelessly from iOS, iPadOS, macOS, and tvOS devices to Apple TV, HomePod, and TVs and speakers that support AirPlay.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any app that plays video or audio people might stream to another device.
  - Building a custom media player with an AirPlay button.
  - Referring to AirPlay or showing the AirPlay icon in your UI or marketing.
- **Rules:**
  - Prefer the system-provided media player; it supports chapter navigation, subtitles, closed captioning, and AirPlay streaming. Design a custom player only if the system one doesn't meet your needs.
  - Provide content in the highest possible resolution: your HLS playlist must include the full range of resolutions so content streamed to a 4K TV doesn't look low quality (content that looks great on iPhone at 720p looks poor on a 4K TV).
  - Stream only the content people expect; don't stream background loops or short in-app video experiences.
  - Support both AirPlay streaming and mirroring.
  - Support remote control events so people can play, pause, and fast forward from the lock screen, Siri, or HomePod.
  - Don't stop playback when your app enters the background or when the device locks, and avoid automatic mirroring.
  - Don't interrupt another app's playback unless your app is starting to play immersive content; auto-playing or launch videos play on the local device only (use the ambient category).
  - Let people use other parts of your app during playback; don't let other in-app videos start and interrupt the stream.
  - If necessary, provide a custom interface for controlling media playback with buttons that match the system ones, including distinct states for starting, active, and unavailable; use only Apple-provided symbols to initiate AirPlay and position the AirPlay icon in the lower-right corner (iOS 16 and iPadOS 16 and later).
  - Icons: use the black AirPlay icon on light backgrounds when other technology icons are black; the white icon on dark backgrounds when others are white; a custom color when other technology icons share that color. Position the AirPlay icon consistently with other technology icons (same shapes if others use shapes).
  - Don't use the AirPlay icon or name in custom buttons or interactive elements; use them only in noninteractive ways.
  - Pair the icon with the name AirPlay correctly (below or beside, same font as your layout); don't use the icon within text or as a replacement for the name.
  - Emphasize your app over AirPlay; references to AirPlay are less prominent than your app name.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS. Not supported in watchOS.
- **Copy/labels:** "AirPlay" is one word with uppercase A and P; all caps only if the whole layout is all caps. Always use AirPlay as a noun: "Use AirPlay to listen on your speaker" (not "AirPlay to your speaker" or "You can AirPlay with [App Name]"). Use "works with", "use", "supports", "compatible": "[App Name] is compatible with AirPlay", "AirPlay-enabled speaker", "You can use AirPlay with [App Name]" (not "[App Name] has AirPlay"). "Compatible with Apple AirPlay" is acceptable. "[App Name] now supports AirPlay" is acceptable when content is specific to AirPlay.
- **APIs:** AVPlayerViewController (AVKit), AVFoundation (`usesExternalPlaybackWhileExternalScreenIsActive`), HTTP Live Streaming, Remote command center events (MediaPlayer), AVAudioSession `ambient` category.
- **Web translation:** Use the native video element with the browser's own remote playback (AirPlay) picker, serve a multi-resolution HLS playlist, don't autoplay into a remote stream, and use the AirPlay name only as a noun with the official icon. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/airplay.md)

### Always On
- **Summary:** On devices that include the Always On display, the system can continue to display an app's interface when people suspend their interactions with the device.
- **Platforms:** ios, watchos
- **When this applies:**
  - watchOS apps that are frontmost or running a background session when the wrist drops.
  - iPhone 14 Pro and iPhone 14 Pro Max Lock Screen widgets and Live Activities when the device is set face up.
  - Any interface that shows personal data, animation, or frequently updating content.
- **Rules:**
  - Hide sensitive information: redact bank balances, health data, and personal information in notifications.
  - Keep other types of personal information glanceable when it makes sense (pace and heart rate during a workout; flight arrival; ride arrival); people can turn off Always On if they want nothing visible.
  - Keep important content legible and dim nonessential content: increase dimming on secondary text, images, and color fills; remove row backgrounds; replace rich images or large color areas with dimmed colors.
  - Maintain a consistent layout: transition interactive components to an unavailable appearance rather than removing them; make infrequent, subtle updates (a sports app updates only when the score changes); motion is especially distracting on a face-up iPhone.
  - Gracefully transition motion to a resting state; don't stop it instantly.
- **Platform notes:**
  - No additional considerations for iOS or watchOS. Not supported in iPadOS, macOS, tvOS, or visionOS.
- **Copy/labels:** n/a
- **APIs:** Designing your app for the Always On state (watchOS apps), Widgets, Live Activities, Notifications, SwiftUI timelines.
- **Web translation:** n/a (no Always On state in browsers). Loosely, respect `prefers-reduced-motion` and avoid exposing sensitive values in persistent lock-screen style notifications. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/always-on.md)

### App Clips
- **Summary:** An App Clip is a lightweight version of your app or game that provides an on-the-go or demo experience that's instantly available.
- **Platforms:** ios, ipados
- **When this applies:**
  - An in-the-moment task at a physical location (rent a bike, order coffee, pay for a meal, museum commentary) or a demo of your app or game before purchase.
  - Designing the App Clip card, App Clip Codes, and printed or digital placement of codes.
  - Deciding how and when to recommend the full app, and how to handle notifications and payments inside the clip.
- **Rules:**
  - Allow people to complete a task or a demo in your App Clip; don't require the full app to finish the demo, task, or level.
  - Focus on essential features; reserve advanced features for the app.
  - Don't use App Clips solely for marketing purposes; don't advertise services or display ads in the clip.
  - Avoid using web views in your App Clip; if only web components are available, offer a link to your website instead.
  - Design a linear, easy-to-use, and focused user interface: no tab bars, complex navigation, or settings; minimal screens and entry forms.
  - On launch, show the most relevant part of your App Clip; skip unnecessary steps.
  - Ensure people can use your App Clip immediately: include all required assets, omit splash screens, never make people wait on launch.
  - Ensure your App Clip is small; reduce code and unused assets; avoid downloading additional data.
  - Make the App Clip shareable (links to specific points; recipients launch from Messages).
  - Make it easy to pay for a service or product; consider Apple Pay for express checkout with no typing.
  - Avoid requiring people to create an account before they can benefit; if required, minimize information, for example with Sign in with Apple.
  - Provide a familiar, focused experience in your app once installed; don't require people to log in again when transitioning from the clip.
  - Privacy: limit the amount of data you store and handle yourself; store login securely off device; don't rely on previously stored data because the system may have removed the clip. Consider offering Sign in with Apple. Offer a secure way to pay that respects privacy, such as Apple Pay. App Clips can't perform background operations.
  - Showcasing: don't compromise the user experience by asking people to install the full app; let people fully experience a demo first. Pick the right time to recommend your app: display an SKOverlay at task completion or a natural pause. Recommend your app in a nonintrusive, polite way: no repeated asks, no interrupting a task, no push notifications for this purpose; communicate additional features clearly.
  - Notifications: App Clips can schedule and receive notifications for up to 8 hours after launch. Only ask for permission to use notifications for an extended period of time if it's really needed (functionality spanning more than a day, such as a car return reminder). Keep notifications focused: no promotional notifications, only in response to an explicit action. Use notifications to help people complete a task (delivery updates).
  - Businesses: a platform provider can power many App Clip experiences with one App Clip. Use consistent branding: tone down your own and feature the business's brand. Consider multiple businesses: handle switching between recent businesses or locations and verify a person's location at launch.
  - App Clip card: be informative; prefer photography and graphics over UI screenshots; avoid using text in the header image (not localizable); adhere to image requirements: 1800x1200 px PNG or JPEG without transparency. Use concise copy: title no more than 30 characters, subtitle no more than 56 characters. Pick a verb for the action button: View (media, informational, or educational content), Play (games), Open (everything else).
  - App Clip Codes: always use Apple's designs; badge design with the App Clip logo, or the design without it when space is tight. Scan-only codes show a camera icon in the center; NFC-integrated codes show an iPhone icon. Use NFC-integrated codes where people can physically reach them (tabletop, register, storefront window, signage, gift card or coupon); use scan-only codes for inaccessible or digital placement (posters, signage behind a counter, digital displays, emails, social media).
  - Include the App Clip logo when space allows; omit it if you can't meet clear space requirements, on disposable paper or plastic items, or on items associated with gambling or drinking (playing cards, poker chips, bar coasters); never use the App Clip logo on its own.
  - Place your App Clip Code on a flat or cylindrical surface only; on a cylinder the code's width must not exceed one-sixth of the circumference.
  - Help your App Clip Code remain as flat as possible; avoid deformable materials (paper, plastic, fabric) or attach the code to something rigid; stickers must adhere well.
  - Place your App Clip Code in a location that helps ensure reliable scanning (enough light, no wide angles).
  - Make sure the App Clip Code is unobstructed: no overlaid text, logos, or images; never animate or dim it.
  - Display the App Clip Code in an upright position; don't rotate the code or the center glyph.
  - Don't create App Clip Codes that are too small: printed minimum diameter 3/4 inch (1.9 cm); digital minimum 256x256 px as PNG or SVG; NFC-integrated codes need an NFC tag at least 35 mm in diameter, so the printed code must be at least 1.37 inches (3.48 cm) in diameter. Use a distance to code size ratio of no more than 20:1, ideally 10:1 (scanned from 40 inches (101 cm) away needs at least 4 inches (10.16 cm) diameter). Next to a QR code or other scannable item, make the App Clip Code at least that item's size.
  - Provide enough space between an App Clip Code and adjacent codes, graphics, or materials: minimum clear space equals the space between the center glyph and the circular code.
  - Use clear messaging near the code, especially without the logo: "Scan to [describe what people can do]"; "Scan using the camera on your iPhone or iPad to [...]"; for NFC: "Hold your iPhone near the [object name] to launch an App Clip that [...]".
  - Adhere to Apple trademark guidelines: no Apple trademarks in your app name or images; title case for "App Clips" and "App Clip Code".
  - Always use the generated App Clip Code (from App Store Connect or the App Clip Code Generator); don't modify it, apply filters, change colors, or add glows, shadows, gradients, or reflections; scale all attributes together without changing aspect ratio.
  - Choose colors with enough contrast; each code uses a foreground, a background, and a generated third color; the tools refuse combinations that scan poorly and can suggest a foreground color.
  - Printing: use high-quality, non-textured matte materials; avoid gloss, reflective or holographic overlays and thin laminates; use matte laminate if needed; UV-resistant materials outdoors; flexographic printing with a service or inkjet on a desktop printer. Rasterize the SVG at least 600 ppi and print at a minimum of 300 dpi; calibrate the printer; with receipt printers print close to the paper's maximum bounds. Convert sRGB to CMYK with relative colorimetric (media-relative) intent, "Generic CMYK ICC profile" on CMYK printers or "Gracol 2013 ICC profile" on CMYKOV printers, color tolerance CIELab Delta E of 2.5. If the printer only prints grayscale, generate grayscale codes. For NFC-integrated codes choose Type 5 NFC tags at least 35 mm in diameter. For large batches, test the workflow with small runs, print templates showing the invocation URL and SVG filename, and track SVG-to-URL mapping. Use Apple's printer calibration test sheets to verify color pairs and grayscale.
  - Legal: only Apple-generated codes that follow the guidelines are approved; stop displaying a code when its clip is inactive; don't use the App Clip Code, Apple logo, or App Clip mark in your company or product name or seek trademark registration; don't add a symbol to the codes; don't translate Apple trademarks.
- **Platform notes:**
  - No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Card title at most 30 characters, subtitle at most 56 characters; action button verb View, Play, or Open; calls to action "Scan to ..." or "Hold your iPhone near the [object name] to launch an App Clip that ..."; title case for App Clips and App Clip Code.
- **APIs:** App Clips framework, SKOverlay (StoreKit), App Store Connect, App Clip Code Generator, Apple Pay, Sign in with Apple, Enabling notifications in App Clips, Configuring App Clip experiences.
- **Web translation:** The closest analogue is a focused, fast-loading single-task web page reached by QR code or NFC: no account wall, express checkout, no ads, and a polite install prompt only after the task completes. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/app-clips.md)

### Apple In-App Purchase
- **Summary:** People can use Apple In-App Purchase to pay for digital goods and services, like premium content and subscriptions, securely within your app.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Selling consumable content (lives, gems), non-consumable content (premium features), auto-renewable subscriptions, or non-renewing subscriptions (a battle pass).
  - Designing paywalls, sign-up screens, offer code redemption, refunds and purchase help, and subscription management.
  - Choosing between Apple In-App Purchase (virtual goods) and Apple Pay (physical goods, services, donations).
- **Rules:**
  - Let people experience your app before making a purchase; consider limited free access to subscription content.
  - Design an integrated shopping experience that mirrors the style of your app.
  - Use simple, succinct product names and descriptions that don't truncate or wrap.
  - Display the total billing price for each in-app purchase you offer, regardless of type.
  - Display your store only when people can make payments (check `canMakePayments`); otherwise hide it or explain why it's unavailable.
  - Use the default confirmation sheet; don't modify or replicate it.
  - Family Sharing (up to five additional family members): prominently mention Family Sharing where people learn about content ("Family" or "Shareable" in a name, mention in sign-up); help people understand the benefits and how to participate; customize messaging for purchasers and family members ("Your family subscription includes...").
  - Providing help: provide help that customers can view before they request a refund (missing purchases, FAQs, feedback, contact). Use a simple title for the refund action, like "Refund" or "Request a Refund". Help people find the problematic purchase (image, name, description, original purchase date). Consider offering alternative solutions (immediate fulfillment, conciliatory item) while making it clear people can still request a refund. Make it easy to request a refund; don't make people scroll or open another screen to reach the button. Avoid characterizing or providing guidance on Apple's refund policies; link to Apple's refund support page instead.
  - Auto-renewable subscriptions: call attention to subscription benefits during onboarding with a strong call to action and a clear summary of terms. Offer a range of content choices, service levels, and durations. Consider letting people try your content for free (freemium, metered paywall, free trial). Prompt people to subscribe at relevant times (nearing a monthly limit) and make subscribing possible at any time. Encourage a new subscription only when someone isn't already a subscriber; offer sign-in so cross-platform subscribers don't pay twice.
  - Signup: provide clear, distinguishable subscription options with short names, price, and duration; for introductory prices list the introductory price, offer duration, and standard price afterward. Simplify initial signup by asking only for necessary information. In tvOS, help people sign up or authenticate using another device (send a code). The in-app sign-up screen must include: subscription name, duration, and content or services per period; billing amount correctly localized for each territory and currency; a way for existing subscribers to sign in or restore purchases; plus links to Terms of Service and Privacy Policy. Clearly describe how a free trial works, including that payment starts automatically when the trial ends. Include a sign-up opportunity in your app's settings.
  - Offer codes (iOS, iPadOS): one-time use codes (unique, generated in App Store Connect, redeemable via URL, in app, or in the App Store) for small or restricted distribution; custom codes (like NEWYEAR or SPRINGSALE, redeemable via URL or in app only) for large campaigns. Clearly explain offer details. Follow guidelines for creating a custom code: only alphanumeric ASCII characters, no special, Chinese, or Arabic characters. Tell people how to redeem a custom code (not via App Store account settings). Consider supporting offer redemption within your app with a "Redeem Code" button on your paywall, onboarding, or settings; the system provides the redemption screens. Supply an engaging and informative promotional image (otherwise your app icon is used). Help people benefit from unlocked content as soon as they complete redemption, including people who subscribed before first opening your app.
  - Managing subscriptions: provide summaries of the customer's subscriptions, especially the upcoming renewal date, near the management option in settings or account. Consider using the system-provided subscription-management UI. Encourage a subscriber to keep their subscription or resubscribe later (remind what they lose, suggest a plan, offer a discount; win-back offers). Always make it easy for customers to cancel an auto-renewable subscription; don't bury or disguise the manage action.
- **Platform notes:**
  - watchOS: the sign-up screen must display the same required information as other versions. Clearly describe the differences between versions of your app on different devices without implying identical experiences. Consider using a modal sheet to display the required information (default Close button returns to free content; a custom view needs Close or Cancel). Make subscription options easy to compare on a small screen: one option per button locked up with its description, or a list of options followed by a button whose title updates to the chosen option.
  - No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.
- **Copy/labels:** Refund action titled "Refund" or "Request a Refund"; "Redeem Code" button; name subscriptions "Family" or "Shareable" when shared; show total billing price everywhere; custom offer codes use alphanumeric ASCII only.
- **APIs:** StoreKit (In-App Purchase, `canMakePayments`, `beginRefundRequest(for:in:)`, `presentOfferCodeRedeemSheet(from:options:)`, SwiftUI `offerCodeRedemption(options:isPresented:onCompletion:)`, Product.SubscriptionInfo, `showManageSubscriptions(in:)`), Retention Messaging API, Advanced Commerce API, App Store Connect offer codes.
- **Web translation:** Show the full billed amount and renewal terms on the plan picker, put a restore or sign-in link on the paywall, state trial end and first charge clearly, keep cancel one click deep in account settings, and never editorialize about refund outcomes. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/apple-in-app-purchase.md)

### Apple Pay
- **Summary:** Apple Pay is a secure, easy way to make payments for physical goods and services, donations, and subscriptions in apps and in any browser.
- **Platforms:** ios, ipados, macos, visionos, watchos
- **When this applies:**
  - Checkout for physical goods, services (memberships, reservations, tickets), donations by approved nonprofits, and recurring payments.
  - Placing and styling Apple Pay buttons and the Apple Pay mark; customizing the payment sheet; handling errors.
  - Referring to Apple Pay in text and on confirmation pages; websites must include a privacy statement and follow the acceptable use guidelines.
- **Rules:**
  - Offer Apple Pay on all devices and browsers that support it; don't present it where unsupported.
  - Make Apple Pay the primary payment option when credentials are available; if you use the APIs to detect an active card you must make Apple Pay primary (not necessarily sole) everywhere you use them; don't separate it into a different step; pre-select it among options.
  - Use Apple Pay buttons only to initiate payment or, when appropriate, the Apple Pay setup process.
  - If you use a custom button to start the payment, make sure it doesn't display "Apple Pay" or the Apple Pay logo; show the Apple Pay mark or reference Apple Pay in text on the same page.
  - Use the Apple Pay mark graphic only to communicate that you accept Apple Pay; never use it as or position it as a button.
  - Don't hide an Apple Pay button or make it appear unavailable; point out missing selections after the tap.
  - Inform search engines that Apple Pay is accepted on your website via semantic markup.
  - Checkout: provide a cohesive checkout experience with your branding, without opening new pages or windows. If Apple Pay is available, assume people want to use it (first, larger, or separated by a line). Accelerate single-item purchases with Apple Pay buttons on product detail pages (purchase that item only; remove it from the cart afterward). Accelerate multi-item purchases with express checkout. Support coupons and promotional codes in the payment sheet. Collect necessary information like color and size before the button, and highlight and navigate to missing fields. Collect optional information (gift messages, delivery instructions) before or after checkout, not on the sheet. Gather multiple shipping methods and destinations before showing the sheet (it supports one per order). For in-store pickup, help people choose a pickup location first and show its address on the sheet. Prefer checkout information from Apple Pay over stored data. Avoid requiring account creation before purchase; offer it on the confirmation page prefilled. Report transaction results in the payment sheet with error messages. Display an order confirmation or thank-you page; if you mention Apple Pay, show it after the last four digits or as a note: "1234 (Apple Pay)" or "Paid with Apple Pay."
  - Payment sheet: only present and request essential information (no shipping address for an electronic gift card). Display the active coupon or promotional code, or let people enter one. Let people choose the shipping method in the sheet with description, cost, and estimated delivery or pickup date range using calendar and time-zone support. For in-store pickup, consider letting people choose a pickup window. Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring and future payments, not an itemized product list. Keep line items short, ideally one line. Provide a business name after the word Pay on the total line matching the card statement: "Pay [Business_Name]". If you're not the end merchant, identify both businesses: "Pay [End_Merchant_Business_Name (via Your_Business_Name)]". Clearly disclose when people may incur additional costs after authorization with a subtotal marked Amount Pending where regulations allow. Handle data entry and payment errors gracefully. Defer to the payment sheet for progress information; don't add spinners.
  - Website icon: provide 60x60 pt icons (120x120 px @2x, 180x180 px @3x) for Handoff and Wallet.
  - Data validation errors: validate when the sheet appears, on field changes, and after authentication; before authorization only card type and a redacted shipping address are available. Avoid forcing compliance with your business logic (accept Zip+4 by ignoring extra digits; accept multiple phone formats). Accurately report problems to the system with custom messages and correct status codes. Explain the problem clearly and succinctly, referencing the field: "Zip code doesn't match city" instead of "Address is invalid"; "Shipping not available for this state"; noun phrases, sentence-style capitalization, no ending punctuation, 128 characters or fewer.
  - Payment processing: handle interruptions correctly; on cancellation or timeout you must cancel any in-progress payment; people restart by choosing the button again.
  - Subscriptions: clarify subscription details before showing the sheet; include line items that reiterate billing frequency, discounts, and upfront fees, and disclose when billing occurs if nothing is due now; clearly communicate trial period terms (trial amount including $0, regular amount, date regular billing begins); clarify the current payment amount in the total line; only show the payment sheet when a subscription change results in additional fees. Treat the billing agreement field as a plain-language summary; leave it blank when in doubt.
  - Donations (approved nonprofits only): use a line item to identify a donation ("Donation $50.00"); offer predefined amounts like $25, $50, $100 plus an Other Amount option.
  - Buttons: always use the Apple-provided API (approved captions, fonts, colors, scaling, localization, corner radius, VoiceOver); never create or replicate custom Apple Pay button designs. Button types and usage: Buy with (product or cart pages), Pay with (bills and invoices), Check Out with and Continue with (when other payment buttons start with those words), Book with (flights, trips), Donate with (approved nonprofits), Subscribe with, Reload with, Add Money with, Top Up with (adding money to a card or account), Order with (meals, flowers), Rent with (cars, scooters), Support with and Contribute with (giving to projects or causes), Tip with, and the plain Apple Pay button (smaller minimum width or no call to action; also the automatic fallback). Set Up Apple Pay button: for devices that support Apple Pay but haven't set it up; show in Settings, a profile, or an interstitial.
  - Styles: automatic follows system appearance; black on white or light backgrounds with sufficient contrast (not on dark); white with outline on white or light backgrounds without sufficient contrast (not on dark or saturated); white on dark backgrounds.
  - Size and position: prominently display the Apple Pay button, no smaller than other payment buttons, without requiring scroll. Place it to the right of an Add to Cart button side by side, or above it when stacked. Adjust the corner radius to match other buttons. Maintain the minimum button size and margins: plain Apple Pay button minimum width 100pt, minimum height 30pt, margins 1/10 of the button's height; Book, Buy, Check Out, Donate, Set Up, and Subscribe buttons minimum width 140pt, minimum height 30pt, margins 1/10 of the height. If the translated title doesn't fit, the system substitutes the plain Apple Pay button (no substitution for Set Up Apple Pay).
  - Apple Pay mark: use only Apple's artwork, altering only height, equal to or larger than other payment brand marks; don't change width, corner radius, or aspect ratio; no trademark symbol, no removed border, no shadows, glows, reflections, flips, rotation, or animation. Maintain minimum clear space of 1/10 of its height; don't share its border with another graphic or button.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, visionOS, or watchOS. Not supported in tvOS. People pay with Face ID, Touch ID, Optic ID, or by double-clicking on Apple Watch; in browsers also with a nearby iPhone or Apple Watch or by scanning a code.
- **Copy/labels:** "Apple Pay" is two words, uppercase A and P; all caps only to match an all-caps style; never plural or possessive; never the Apple logo in place of "Apple"; in the United States use ® on first mention in body text but not in checkout selection options; don't mimic Apple typography; never translate Apple Pay. Correct: "Purchase with Apple Pay", "Purchase with Apple Pay®". Incorrect: "Purchase with ApplePay", "Purchase with  Pay" (logo), "Purchase with APPLE PAY". A text-only description of Apple Pay is allowed in a payment selection only when all options are text-only; otherwise use the mark. Total line reads "Pay [Business_Name]". Confirmation may read "1234 (Apple Pay)" or "Paid with Apple Pay."
- **APIs:** PassKit (PKPaymentAuthorizationController, PKPaymentAuthorizationViewControllerDelegate, PKPaymentRequest `paymentSummaryItems`, PKDateComponentsRange, PKPaymentError, PKPaymentButtonType, PKPaymentButtonStyle, PKPaymentButton `cornerRadius`), WKInterfacePaymentButton (WatchKit), Apple Pay on the Web (ApplePaySession `applePayCapabilities`, ApplePayButtonStyle, `oncancel`, Apple Pay Status Codes), Displaying a Read-Only Pickup Address.
- **Web translation:** Apple Pay on the Web is itself the web path: use the Apple Pay JS button API, detect availability before showing it, keep checkout in one page, validate fields with specific sentence-case messages under 128 characters, and follow the same mark and wording rules. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/apple-pay.md)

### Augmented reality
- **Summary:** Augmented reality (or AR) lets you deliver immersive, engaging experiences that seamlessly blend virtual objects with the real world.
- **Platforms:** ios, ipados, visionos
- **When this applies:**
  - Any ARKit-based feature in iOS or iPadOS: placing objects, measuring, image or object detection, multiuser sessions.
  - Coaching, relocalization, error messaging, and the AR glyph and badges in product catalogs.
  - visionOS apps using ARKit for surfaces, hand positions, and nearby physical objects (with permission).
- **Rules:**
  - Offer AR features only on capable devices; if AR is your primary purpose, require ARKit-capable devices; otherwise don't show an error, just don't offer the feature on unsupported devices.
  - Let people use the entire display; avoid cluttering the screen with controls.
  - Strive for convincing illusions when placing realistic objects (scale, surfaces, lighting, camera grain, top-down shadows); update scenes 60 times per second so objects don't jump or flicker.
  - Consider how virtual objects with reflective surfaces show the environment; prefer small or coarse reflective surfaces.
  - Use audio and haptics to enhance the immersive experience (contact sounds, bumps, background music).
  - Minimize text in the environment.
  - If additional information or controls are necessary, consider displaying them in screen space (fixed location).
  - Consider using indirect controls (2D, in screen space, translucent, reachable without adjusting grip) for persistent controls, as Measure does.
  - Anticipate that people will use your app in a wide variety of real-world environments; communicate requirements up front; consider different feature sets for different environments.
  - Be mindful of people's comfort: place objects at distances that reduce device movement; keep game levels short with downtime.
  - If your app encourages people to move, introduce motion gradually.
  - Be mindful of people's safety; avoid encouraging large or sudden movements.
  - Coaching: use the built-in coaching view for initialization and relocalization. Hide unnecessary app UI while people are using a coaching view. If necessary, offer a custom coaching experience modeled on the system one.
  - Placing objects: show people when to locate a surface and place an object with an indicator aligned to the detected plane. When people place an object, immediately integrate that object into the AR environment, then subtly refine position (nudge back onto the surface). Consider guiding people toward offscreen virtual objects with visual or audible cues. Avoid trying to precisely align objects with the edges of detected surfaces. Incorporate plane classification (only place furniture on "floor", a game board on "table").
  - Interactions: let people use direct manipulation to interact with objects when possible; indirect controls work better when people move around. Let people directly interact with virtual objects using standard, familiar gestures (single-finger drag to move, two-finger rotation). In general, keep interactions simple: limit movement to the surface plane and rotation to a single axis. Respond to gestures within reasonable proximity of interactive virtual objects. Let people initiate object scaling when it makes sense (imaginary environments, not furniture shopping); don't use scaling to adjust distance. Be wary of potentially conflicting gestures (pinch versus rotate). Strive for virtual object movement that's consistent with the physics of your AR environment; keep objects attached to surfaces and visible. Explore even more engaging methods of interaction (motion, proximity).
  - Multiuser: consider allowing people occlusion; when possible, let new participants enter a multiuser AR experience via implicit map merging.
  - Real-world objects: when a detected image first disappears, consider delaying the removal of attached virtual objects, waiting up to one second before fading. Limit the number of reference images in use at one time to 100 or fewer; swap sets by context. Limit the number of reference images requiring an accurate position (use tracked images only when the image may move or the attached content is small).
  - Communicating: if you must display instructional text, use approachable terminology; avoid ARKit, world detection, tracking, plane, anchor, features. Do: "Unable to find a surface. Try moving to the side or repositioning your phone." "Tap a location to place the [object]." "Try turning on more lights and moving around." "Try moving your phone more slowly." Don't: "Unable to find a plane. Adjust tracking." "Tap a plane to anchor an object." "Insufficient features." "Excessive motion detected."
  - In a three-dimensional context, prefer 3D hints (a rotation indicator around an object); use 2D text hints only if people aren't responding.
  - Make important text readable: critical labels and instructions in screen space; 3D text faces the person with the same type size regardless of distance.
  - If necessary, provide a way to get more information with a visual indicator people can tap.
  - Interruptions: consider using the system coaching view to help people relocalize. Consider hiding previously placed virtual objects during relocalization. Minimize interruptions if your app supports both AR and non-AR experiences (embed the non-AR task in AR, such as changing upholstery). Allow people to cancel relocalization with a reset button. Indicate when the front-facing camera is unable to track a face for more than about half a second, with minimal text.
  - Problem resolution: let people reset the experience if it doesn't meet their expectations. Suggest possible fixes: insufficient features, "Try turning on more lights and moving around."; excessive motion, "Try moving your phone slower."; slow surface detection, "Try moving around, turning on more lights, and making sure your phone is pointed at a sufficiently textured surface."
  - Icons and badges: use the AR glyph as intended, strictly for initiating ARKit-based experiences; alter only size and color. Maintain minimum clear space of 10% of the glyph's height. Use the AR badges as intended and don't alter them (collapsed and expanded forms, never recolored, only for ARKit experiences). Prefer the AR badge to the glyph-only badge; use glyph-only for constrained spaces. Use badging only when your app contains a mixture of objects that can and can't be viewed in AR. Keep badge placement consistent and clear in the same corner of each photo. Maintain minimum clear space of 10% of the badge's height.
- **Platform notes:**
  - visionOS: with the wearer's permission, use ARKit to detect surfaces, use hand and finger positions for custom gestures, and incorporate nearby physical objects into immersive experiences.
  - No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, or watchOS.
- **Copy/labels:** Friendly, nontechnical instruction text as quoted above; a "View in AR" button uses the AR glyph; AR badges labeled "AR".
- **APIs:** ARKit (ARCoachingOverlayView, ARTrackedRaycast, ARWorldTrackingConfiguration `isCollaborationEnabled`, people occlusion, image detection, session life cycle), Playing audio, Playing haptics, Gestures.
- **Web translation:** For WebXR or model-viewer AR, feature-detect before showing an "View in AR" affordance, keep UI minimal and screen-fixed, use friendly non-technical error text, and offer a reset action. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/augmented-reality.md)

### CareKit
- **Summary:** People can use CareKit apps to manage care plans related to a chronic illness like diabetes, recover from an injury or surgery, or achieve health and wellness goals.
- **Platforms:** ios, ipados
- **When this applies:**
  - Apps that present care plans: tasks (medication, therapy, symptom logging), charts of progress, and care team contacts.
  - Integrating HealthKit, motion data, photos, or ResearchKit into a care app.
  - Notifications and branding inside a care app.
- **Rules:**
  - Data and privacy: provide a coherent privacy policy URL at submission. Get permission before accessing data through iOS features and protect all data.
  - HealthKit: request access to health data only when you need it (weight when logging weight, not at launch) and request every time you need access because permissions can change. Clarify your app's intent by adding descriptive messages to the standard permission screen; don't replicate it with custom screens. Manage health data sharing solely through the system's privacy settings (Settings > Privacy).
  - Motion data (with permission) can report standing still, walking, running, cycling, driving, step count, pace, and flights of stairs; photos (with permission) can document treatment progress; ResearchKit can supply surveys, tasks, charts, and informed consent.
  - Views: use each view category for its intended purpose: Tasks (prescribed actions and logging), Charts (progress), Contact views (care team communication). A view has a header (text, symbol, disclosure indicator, separator) and a content stack.
  - Tasks carry a Title (required, like Ibuprofen), Schedule (required, like Four times a day), Instructions (optional), and Group ID (optional, like medication or exercise). Use the simple style for a one-step task; use the instructions style when you need to add informative text to a simple task ("Take on an empty stomach"); use the log style to help people log events (timestamps per log); use the checklist style for a multistep task with descriptions; use the grid style for a compact multistep task with short button titles (custom UI allowed in its collection view).
  - Consider using color to reinforce the meaning of task items, never as the only way to convey information.
  - Combine accuracy with simplicity when describing a task and its steps (marketing name of a medication; omit repeated words like take).
  - Consider supplementing multistep or complex tasks with videos or images.
  - Charts (bar, scatter, line; title, subtitle, axis markers, dataset): consider highlighting narratives and trends to illustrate progress; label chart elements clearly and succinctly (BPM in the axis label, not every point); use distinct colors with sufficient contrast; consider providing a legend; clearly denote units of time; consolidate large data sets; if necessary, offset data to keep charts proportional.
  - Contact views (simple and detailed): consider using color to categorize care team members.
  - Notifications: minimize notifications and consider coalescing items into one; consider providing a detail view so people can mark tasks complete without opening the app.
  - Symbols and branding: most views work best with CareKit-provided symbols; use SF Symbols for custom items in grid views. Design a relevant care symbol (closely related to health and wellness; no decorative symbols or corporate logos). Incorporate refined, unobtrusive branding through color and communication style; no advertising.
- **Platform notes:**
  - No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Task titles are short (medication marketing names); schedules read like "Four times a day"; instructions like "Take 1 tablet every 4-6 hours (not to exceed 4 tablets daily)."; permission screen messages are a few succinct sentences on why and how people benefit.
- **APIs:** CareKit (CareKit UI, CareKit Store, Chart Interfaces), HealthKit (`requestAuthorization(toShare:read:completion:)`, Protecting user privacy), Core Motion, UIImagePickerController (UIKit), ResearchKit, SF Symbols, Notifications.
- **Web translation:** For a web care app, present tasks as checklists with clear schedules, charts with labeled units and a legend, minimal notifications, and a prominent privacy policy; request health data only in context. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/carekit.md)

### CarPlay
- **Summary:** CarPlay lets people get directions, make calls, send and receive messages, listen to music, and more from their car's built-in display, all while staying focused on the road.
- **Platforms:** ios
- **When this applies:**
  - iPhone apps in supported categories (audio, communication, navigation, and others) that render through system templates on the car display.
  - Audio behavior alongside the car radio and navigation prompts.
  - Icon, color, layout, and error handling for the car display.
- **Rules:**
  - Use the system-defined templates for your app type; the system renders UI and handles the vehicle hardware (touchscreens, knobs, touch pads).
  - Eliminate app interactions on iPhone when CarPlay is active; do setup before the vehicle is in motion.
  - Never lock people out of CarPlay because the connected iPhone requires input; let them resolve problems after the vehicle stops.
  - Make sure your app works without requiring people to unlock iPhone.
  - Audio: let people choose when to start playback (no autoplay unless your purpose is a single audio source or you're resuming); don't start an audio session until you're ready to play because it silences other sources like the radio. Start playback as soon as audio has sufficiently loaded (the system shows a spinner until you signal readiness). Display the Now Playing screen when audio is ready to play; load descriptive information in the background. Resume audio playback after an interruption only when it's appropriate (resume after a phone call; not after a Siri-initiated playlist). When necessary, automatically adjust audio levels, but don't change the overall volume.
  - Layout: common display sizes are 800x480 (5:3), 960x540 (16:9), 1280x720 (16:9), and 1920x720 (8:3) pixels. Provide useful, high-value information in a clean layout that's easy to scan from the driver's seat. Maintain an overall consistent appearance. Ensure that primary content stands out and feels actionable; large items; most important content and controls in the upper half of the screen.
  - Color: in general, prefer a limited color palette that coordinates with your app logo. Avoid using the same color for interactive and noninteractive elements. Test your app's color scheme under a variety of lighting conditions in an actual car (night brightness, sunlight washout). Ensure your app looks great in both dark and light environments. Choose colors that help you communicate effectively with everyone.
  - Icons and images: supply high-resolution images with scale factors of @2x and @3x for all CarPlay artwork. Mirror your iPhone app icon. Don't use black for your icon's background (lighten it or add a border). App icon sizes: 120x120 px @2x and 180x180 px @3x.
  - Error handling: report errors in CarPlay, not on the connected iPhone; never direct people to pick up their iPhone.
- **Platform notes:**
  - No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS. CarPlay audio and video apps also work on Apple HomeView without modification.
- **Copy/labels:** n/a
- **APIs:** CarPlay framework templates (CarPlay App Programming Guide), Now Playing, Live Activities and widgets for CarPlay and CarPlay Ultra.
- **Web translation:** n/a (no web surface in CarPlay).
- **Source:** [reference](../references/technologies/carplay.md)

### Game Center
- **Summary:** Game Center is Apple's social gaming network, which lets players track their progress and connect with friends across Apple platforms, and boosts the discovery of your game across players' devices.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Games adding the access point, achievements, leaderboards, challenges, or multiplayer activities.
  - Producing artwork at the required sizes and using correct Game Center terminology in custom UI.
  - Game Overlay (iOS, iPadOS, macOS) and dashboard (visionOS, tvOS) behavior.
- **Rules:**
  - Determine whether the player is signed in to Game Center at launch and initialize if not, for the most seamless experience and best discovery (Top Played chart, friend recommendations).
  - Display the access point in menu screens (main menu or settings); avoid it during gameplay, splash screens, cinematics, or tutorials.
  - Avoid placing controls near the access point; it sits in any of the four corners and has collapsed and expanded versions.
  - Consider pausing your game while the Game Overlay or dashboard is present.
  - Custom UI: use the artwork Game Center provides in custom links without adjusting dimensions or effects. Use the correct terminology.
  - Achievements: align with Game Center achievement states (locked, in-progress, hidden, completed). Determine a display order (upload order is display order). Be succinct when describing achievements: title and description are limited to two lines each; title-style capitalization for the title, sentence-style for the description. Give players a sense of progress with progressive achievements.
  - Achievement images: design rich, high-quality images; don't reuse one asset for multiple achievements. Create artwork in the appropriate size and format with content centered for the circular mask: iOS, iPadOS, macOS, visionOS: PNG, TIF, or JPG; sRGB or P3; 72 DPI minimum; 512x512 pt (1024x1024 px @2x); mask diameter 512 pt (1024 px @2x). tvOS: 320x320 pt (640x640 px @2x); mask diameter 200 pt (400 px @2x).
  - Leaderboards: choose a leaderboard type: classic (all-time best, never ends) or recurring (resets on an interval such as daily or weekly). Take advantage of leaderboard sets to group boards (difficulty modes, activity types, genres). Add leaderboard images, a unique one per leaderboard: iOS, iPadOS, macOS: JPEG, JPG, or PNG; sRGB or P3; 72 DPI minimum; 512x512 pt (1024x1024 px @2x); cropped area 512x312 pt (1024x624 px @2x). tvOS (a set of layered images that animate on focus): 659x371 pt (1318x742 px @2x); focused size 618x348 pt (1236x696 px @2x); unfocused size 548x309 pt (1096x618 px @2x). Keep primary content clear of cropping.
  - Challenges (built on leaderboards, time-limited, with friends): create engaging challenges that take 1-5 minutes to play and can be completed individually (fastest lap, most enemies in a round, daily puzzle with fewest mistakes). Avoid creating challenges that track overall progress or personal best scores; track the most recent score per attempt. Make it easy to jump into your challenge: deep-link to the exact mode or level and route first-time players through required onboarding with UI explaining the game will jump into the challenge afterward. Create high-quality artwork that encourages engagement; keep primary content away from where the title and description overlay; localize any text in the image. Challenge image: JPEG, JPG, or PNG; sRGB or P3; 72 DPI minimum; 1920x1080 pt (3840x2160 px @2x); cropped area 1465x767 pt (2930x1534 px @2x).
  - Multiplayer activities: use party codes (alphanumeric, typically eight characters, like "2MP4-9CMF") to invite players; allow players to join late, leave early, and return; show the current party code in your game; allow manual code entry. Support multiplayer activities through in-game UI (Game Overlay and dashboard invite nearby or recent players, friends, and contacts). Provide engaging activity artwork: JPEG, JPG, or PNG; sRGB or P3; 72 DPI minimum; 1920x1080 pt (3840x2160 px @2x); cropped area 1465x767 pt (2930x1534 px @2x).
- **Platform notes:**
  - tvOS: display an optional image at the top of the dashboard (logo or word mark, not your app icon): 600x180 pt (1200x360 px @2x); PNG, TIF, or JPG; sRGB or P3; 72 DPI minimum.
  - watchOS: GameKit APIs are available, but there's no system Game Center UI on watchOS; Game Center content appears on a connected iPhone.
  - No additional considerations for iOS, iPadOS, macOS, or visionOS.
- **Copy/labels:** Use "Game Center" (not GameKit, GameCenter, game center) with the system-provided translation; "Game Center Profile" (not Profile, Account, Player Info), localizing Profile; "Achievements" (not Awards, Trophies, Medals); "Leaderboards" (not Rankings, Scores, Leaders); "Challenges" (not Competitions); "Add Friends" (not Add, Add Profiles, Include Friends). Achievement titles in title case, descriptions in sentence case, two lines maximum each.
- **APIs:** GameKit (access point, achievements, leaderboards, challenges, activities, matchmaking), Game Overlay, Apple Games app, App Store Connect, Game Porting Toolkit.
- **Web translation:** n/a for Game Center itself; a web game should still keep social UI out of active gameplay, use consistent names for achievements and leaderboards, and generate short shareable party codes. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/game-center.md)

### Generative AI
- **Summary:** Generative AI empowers you to enhance your app or game with dynamic content and offer intelligent features that unlock new levels of creativity, connection, and productivity.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any feature that creates or transforms text, images, or other content with a generative model (writing tools, image generation, AI dialog in a game).
  - Choosing between on-device and server models and handling personal data.
  - Designing prompts, outputs, latency, feedback, and disclosure.
- **Rules:**
  - Design your experience responsibly: inclusive, designed with care, privacy protecting; small input changes produce very different outcomes and you can't anticipate every request.
  - Keep people in control: honor in-scope requests, handle sensitive content carefully, let people dismiss unwanted content and revert or retry transformations, and clearly identify when and where you use AI.
  - Ensure an inclusive experience for all: ask people for the information a feature needs instead of inferring personal or cultural characteristics; seek clarity before assumptions about gender identities or relationship types; test across diverse people.
  - Design engaging and useful generative features only where they provide clear, specific value.
  - Ensure a great experience even when generative features aren't available or people opt not to use them; offer a non-AI fallback when possible (Genmoji alongside regular emoji; notifications readable without summaries).
  - Transparency: communicate where your app uses AI; never trick someone into thinking they're interacting with or viewing content authored by a human; follow regional disclosure regulations. Set clear expectations about what your AI-powered feature can and can't do (brief tutorial, curated suggestions for open-ended prompts, up-front limitations, how to get good results).
  - Privacy: choose a model type that fits your feature's needs and protects privacy; on-device models keep data local, respond quickly, and work offline; for server-based processing, process locally where possible, minimize what's shared, tell people data may go to a server, show what's shared, and explain off-device storage or training use. Ask permission before using personal information and usage data; use the minimum; offer a clear opt out; get explicit permission for model improvement or storage; understand third parties' privacy; outputs can leak sensitive data; kids apps have stricter rules. Clearly disclose how your app and its model use and store personal information, including whether personal information trains or improves the model.
  - Models and datasets: thoughtfully evaluate model capabilities early; some models may be unavailable due to device compatibility, network, or battery (Foundation Models requires a compatible device with Apple Intelligence on). Be intentional when choosing or creating a dataset: diverse representation, known provenance, proper licenses, time to test for bias and misinformation.
  - Inputs: guide people on how to use your generative feature with diverse predefined example inputs. Raise awareness about and minimize the chance of hallucinations: communicate that AI-generated content may contain errors, scope requests carefully, avoid requesting factual information unless the model has verified, up-to-date data, and avoid AI content where a hallucination could harm someone. Consider consequences and get permission before performing irreversible or potentially problematic tasks: don't automate destructive actions like deleting photos or hard-to-undo actions like purchases; ask for confirmation before significant actions; follow model usage policies and regional AI regulation.
  - Outputs: make it easy for people to refine or revert generated results (Edit, Undo, Retry, Adjust near the content) and acknowledge when corrections take effect. Help people improve requests when blocked or undesirable results occur (Image Playground says "Unable to use that description."); offer example requests. Reduce unexpected and harmful outcomes with thoughtful design and thorough testing of out-of-scope, vague, sensitive, and adversarial requests. Strive to avoid replicating copyrighted content (build on protective models, curate inputs, pre-approved prompts, instruct the model to avoid certain content or styles). Factor processing time into your design; generative models have higher latency than Vision or ARKit body tracking, so design a loading experience or generate in the background. Consider giving specific, reassuring feedback during generation ("Finding substitutions for ingredients", "Summarizing key themes from your notes" rather than "Processing..."); on failure describe what happened plainly with a next step. Consider offering alternate versions of results so people can choose.
  - Continuous improvement: consider ways to improve your model over time (blocked word lists independent of releases; fine-tuning, retesting, and prompt engineering on base model upgrades). Let people share feedback on outputs voluntarily, in a clear location that doesn't interrupt (thumbs up and down, plus detailed feedback). Design flexible, adaptable features that let you swap models.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Label AI-generated content and features as such; use specific progress messages instead of "Processing..."; blocked-result messaging like "Unable to use that description."; controls named Edit, Undo, Retry, Adjust.
- **APIs:** Foundation Models framework, Core AI, Apple Intelligence and machine learning, Vision, ARKit body tracking, Loading pattern, Requesting permission.
- **Web translation:** Disclose AI involvement in the UI, show specific streaming progress text, provide Undo, Retry, and Edit next to generated output, confirm before any irreversible or purchasing action, offer thumbs up and down feedback, and tell people when prompts leave the device. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/generative-ai.md)

### HealthKit
- **Summary:** HealthKit is the central repository for health and fitness data in iOS, iPadOS, and watchOS.
- **Platforms:** ios, ipados, watchos
- **When this applies:**
  - Health and fitness apps that read or write health data (don't request health data if your app has no health or fitness functionality).
  - Displaying Activity rings.
  - Showing the Apple Health icon or referring to Apple Health in text.
- **Rules:**
  - Privacy: you must request permission and protect the data; provide a coherent privacy policy URL at submission.
  - Request access to health data only when you need it (weight when logging weight, not at launch); request every time your app needs access because permissions can change.
  - Clarify your app's intent by adding descriptive messages to the standard permission screen (a few succinct sentences on why and how people benefit); don't replicate the standard screen.
  - Manage health data sharing solely through the system's privacy settings (Settings > Privacy).
  - Activity rings: use Activity rings for Move, Exercise, and Stand information only; never show those metrics in another ring-like element. Use Activity rings to show progress for a single person, clearly identified (label, photo, avatar). Don't use Activity rings for ornamentation (labels, backgrounds). Don't use Activity rings for branding (app icon, marketing). Maintain Activity ring and background colors; no filters, color changes, or opacity changes; design the surrounding interface to blend (enclose in a circle); scale appropriately. Maintain Activity ring margins: minimum outer margin no less than the distance between rings; never crop or encroach; to show within a circle adjust the enclosing view's corner radius rather than masking. Differentiate other ring-like elements from Activity rings with padding, lines, labels, color, or scale. Provide app-specific information only in Activity notifications; don't repeat system Move, Exercise, and Stand updates and never show an Activity ring in your notifications.
  - Apple Health icon: use only the Apple-provided icon. Display the name Apple Health close to the icon. Display the icon consistently with other health-related app icons, no smaller than others. Don't use the Apple Health icon as a button. Don't alter its appearance (no mask, corner radius change, circle, borders, overlays, gradients, shadows). Maintain minimum clear space of 1/10 of its height; don't composite it onto another graphic. Don't use the icon within text or as a replacement for the terms Health, Apple Health, or HealthKit. Don't display Health app images or screenshots (copyrighted).
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, or watchOS. Not supported in macOS, tvOS, or visionOS.
- **Copy/labels:** Refer to the Health app as "Apple Health" or "the Apple Health app"; don't use the term "HealthKit" in user-facing text (say your app "works with the Apple Health app" or "uses data from the Apple Health app"); "Apple Health" is two words with uppercase A and H, all caps only to match an all-caps style; use the system-provided translation of "Health".
- **APIs:** HealthKit (`requestAuthorization(toShare:read:completion:)`, Protecting user privacy, Medications API, workout zones), HKActivityRingView (HealthKitUI), Works with Apple Health badge, Apple Design Resources.
- **Web translation:** n/a for HealthKit access from browsers. If you reference Apple Health on a website, follow the same icon and naming rules ("Apple Health", not "HealthKit"). (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/healthkit.md)

### HomeKit
- **Summary:** HomeKit lets people securely control connected accessories in their homes using Siri or the Home app on iPhone, iPad, Apple Watch, and Mac.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Accessory manufacturer apps and smart home apps that set up, name, organize, configure, or control HomeKit accessories.
  - Suggesting Siri commands, zones, service groups, and scenes.
  - Using the HomeKit icon and referring to HomeKit or the Apple Home app.
- **Rules:**
  - Use HomeKit's terminology and object model: home (root; people can have multiple), room (a name like Bedroom), accessory (physical device) with a category (thermostat, fan, light), service (a controllable feature; never say "service" in UI, use names like garage door opener), characteristic (a controllable attribute; never say "characteristic", say speed or brightness), service group (like "reading lamps"), action (changing a characteristic), scene (a group of actions; the API says action set but UI always says scene), automation, zone (multiple rooms like upstairs).
  - Acknowledge the hierarchical model that HomeKit uses, even if your UI isn't organized by rooms and zones.
  - Make it easy for people to find an accessory's related HomeKit details (room, zone) in an accessory detail view.
  - Recognize that people can have more than one home.
  - Don't present duplicate home settings; defer to the Home app's settings.
  - Setup: use the system-provided setup flow (names, networks, pairing, room and category, favorites in a few steps). Provide context to explain why you need access to Home data with a purpose string such as "Lets you control this accessory with the Apple Home app and Siri across your Apple devices." Don't require people to create an account or supply personal information; make any account optional and after HomeKit setup. Honor people's setup choices; don't force other platforms during HomeKit setup. Carefully consider how and when to provide a custom accessory setup experience: system flow first, then a custom post-setup experience for unique features.
  - Names: suggest service names that suit your accessory; never suggest company names or model numbers. Check that the names people provide follow HomeKit naming rules: only alphanumeric, space, and apostrophe characters; start and end with an alphabetic or numeric character; no emojis ("Reading lamp" and "2nd garage door" are fine; emoji lamp and "#2 garage door" are not); explain problems and suggest alternatives. Help people avoid creating names that include location information ("kitchen light"); suggest assigning the accessory to the room instead.
  - Siri: present example voice commands using the chosen service name right after setup. After setup, consider teaching people about more complex Siri commands in context (You can say "Hey Siri, set 'Movie Time.'"). Recommend that people create zones and service groups if they make sense for your accessory. Offer shortcuts only for accessory-specific functionality that HomeKit doesn't support (like "Order AC filters"). If your app supports both HomeKit and shortcuts, help people understand the difference; never encourage a shortcut for something HomeKit already does.
  - Custom functionality: be clear about what people can do in your app and when they might want to use the Home app (build a scene with your accessory, then suggest adding shades and TV in the Home app). Defer to HomeKit if your database differs; reflect Home app changes automatically and present conflicts visually (both names side by side). Ask permission to update the HomeKit database when people make changes in your app; never overwrite settings without explicit direction.
  - Cameras: don't block camera images with other content; show a microphone button only if the camera supports bidirectional audio.
  - Icons: use only Apple-provided HomeKit and Apple Home app icons. Black icon on light backgrounds with other black technology icons; white on dark; custom color when others share it. Position the HomeKit icon consistently with other technology icons. Use the HomeKit icon noninteractively (no custom buttons titled HomeKit; the Apple Home app icon may open the App Store product page). Don't use the HomeKit icon within text or as a replacement for the word HomeKit. Pair the icon with the name HomeKit correctly (below or beside, same font).
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Emphasize your app over HomeKit. Follow trademark rules: Apple trademarks not in your app name or images; singular, never possessive; don't translate Apple, Apple Home, HomeKit; no category descriptors (say iPad, not tablet; "from your iPhone or iPad" not "from your iOS devices"); no implied sponsorship; correct credit lines in legal information; refer to devices and operating systems only in technical specifications. "HomeKit" is one word with uppercase H and K; "Apple Home" is two words with uppercase A and H. Don't use HomeKit as a descriptor: "[Brand] lightbulbs work with HomeKit.", "HomeKit-enabled thermostat.", "You can use HomeKit with [App Name]." (not "HomeKit lightbulbs."). Don't suggest HomeKit performs an action: "Back door is unlocked with HomeKit." (not "HomeKit unlocked the back door."). "Compatible with Apple HomeKit." and "Open HomeKit settings." are acceptable. Use "Apple Home" on first mention of the app, then "the Home app"; never "Open Home."
- **APIs:** HomeKit (`performAccessorySetup(using:completionHandler:)`), Matter support, Siri, App Shortcuts, MFi portal.
- **Web translation:** n/a for device control from a browser. Marketing pages should follow the same wording and icon rules for HomeKit and Apple Home. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/homekit.md)

### iCloud
- **Summary:** iCloud is a service that lets people seamlessly access the content they care about from any device, without performing explicit synchronization.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Apps that store documents, settings, app state, or game saves across devices.
  - Handling iCloud being unavailable, document deletion, conflicts, and search.
- **Rules:**
  - Make it easy to use your app with iCloud; people expect it to work automatically; if you offer a choice, show a simple all-or-nothing option the first time the app opens.
  - Avoid asking which documents to keep in iCloud; perform file management automatically.
  - Keep content up to date when possible, balancing storage and bandwidth; for very large documents let people control downloads, indicate when a newer version exists, and give subtle feedback if a download takes more than a few seconds.
  - Respect iCloud storage space; store only what people create and understand, not regenerable resources; be picky about the Documents folder because backups include it.
  - Make sure your app behaves appropriately when iCloud is unavailable; no alert, but unobtrusively note that changes won't sync until access is restored.
  - Keep app state information in iCloud (last page viewed) and only settings people want on all devices.
  - Warn about the consequences of deleting a document (removed from iCloud and all devices); ask for confirmation.
  - Make conflict resolution prompt and easy; resolve automatically where possible, otherwise show an unobtrusive notification that differentiates versions.
  - Include iCloud content in search results.
  - For games, consider saving player progress in iCloud with the GameSave framework, which provides built-in alerts for offline syncing issues and conflicts (or build custom UI on GameSave data).
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** A deletion warning explains that the document is removed from iCloud and all other devices.
- **APIs:** CloudKit, GameSave.
- **Web translation:** Sync automatically without a manual sync button, show a quiet offline indicator instead of an alert, confirm deletions that propagate everywhere, and surface version conflicts inline with both versions visible. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/icloud.md)

### ID Verifier
- **Summary:** ID Verifier lets your iPhone app read mobile IDs in person without requiring external hardware.
- **Platforms:** ios
- **When this applies:**
  - iPhone apps (iOS 17 and later) that verify a customer's age or identity in person from an ISO18013-5 mobile ID (venues, rentals).
  - Choosing a Display Only request (data stays in system UI) or a Data Transfer request (requires an additional entitlement and a legal verification requirement).
- **Rules:**
  - Ask only for the data you need; for an age check use an age threshold request (`ageAtLeast(_:)`), not current age or birth date.
  - If your app qualifies for Apple Business Register, register for ID Verifier so your official organization name and logo appear on customers' devices.
  - Provide a button that initiates the verification process labeled Verify Age (simple age check) or Verify Identity (detailed identity request); avoid symbols that specify a communication type like NFC or QR codes; never include the Apple logo in a button label.
  - In a Display Only request, help the person using your app provide feedback on the visual confirmation (buttons like Matches Person and Doesn't Match Person).
- **Platform notes:**
  - No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Button labels "Verify Age" or "Verify Identity"; confirmation buttons "Matches Person" and "Doesn't Match Person"; no Apple logo in buttons.
- **APIs:** ProximityReader (MobileDriversLicenseDisplayRequest, MobileDriversLicenseDataRequest, MobileDriversLicenseRawDataRequest, Adopting the Verifier API), Apple Business Register.
- **Web translation:** n/a (requires iPhone hardware).
- **Source:** [reference](../references/technologies/id-verifier.md)

### iMessage apps and stickers
- **Summary:** An iMessage app can help people share content, collaborate, and even play games with others in a conversation; stickers are images that people can use to decorate a conversation.
- **Platforms:** ios, ipados
- **When this applies:**
  - Building a standalone or extension-based iMessage app or sticker pack.
  - Designing compact and expanded views, icons, and sticker assets.
- **Rules:**
  - Prefer providing one primary experience in your iMessage app; create separate apps for different functionality.
  - Consider surfacing content from your iOS or iPadOS app (shopping list, itinerary) or supporting a simple collaborative task.
  - Present essential features in the compact view (below the transcript); reserve more for the expanded view.
  - In general, let people edit text only in the expanded view, because the compact view is about keyboard-sized.
  - Create stickers that are expressive, inclusive, and versatile; legible on many backgrounds and when rotated or scaled; transparency helps integration.
  - For each sticker, provide a localized alternative description for VoiceOver.
  - Icon sizes (square-cornered; the system rounds corners): Messages and notifications 148x110, 143x100, 120x90 (180x135 @3x), 64x48 (96x72 @3x), 54x40 (81x60 @3x) px @2x; Settings 58x58 @2x and 87x87 @3x; App Store 1024x1024.
  - Sticker sizes: pick one size per pack and don't mix; @3x dimensions: Small 300x300 px, Regular 408x408 px, Large 618x618 px. A sticker file must be 500 KB or smaller. Formats: PNG (8-bit transparency, no animation), APNG (8-bit transparency, animation), GIF (single-color transparency, animation), JPEG (no transparency, no animation).
- **Platform notes:**
  - No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Localized alt text for every sticker.
- **APIs:** Messages framework (MSStickerSize), Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime.
- **Web translation:** n/a.
- **Source:** [reference](../references/technologies/imessage-apps-and-stickers.md)

### Live Photos
- **Summary:** Live Photos lets people capture favorite memories in a sound- and motion-rich interactive experience that adds vitality to traditional still photos.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **When this applies:**
  - Photo apps that display, edit, or share Live Photos.
  - Showing Live Photos in environments that don't support them.
- **Rules:**
  - Apply adjustments to all frames; if you can't, offer converting to a still photo.
  - Keep Live Photo content intact; don't disassemble frames or audio.
  - Implement a great photo sharing experience: preview the entire Live Photo before sharing and always offer sharing as a traditional photo.
  - Clearly indicate when a Live Photo is downloading and when it's playable (progress indicator and completion indication).
  - Display Live Photos as traditional photos in environments that don't support Live Photos; don't imitate the experience.
  - Make Live Photos easily distinguishable from still photos with a hint of movement (custom motion effect); where movement isn't possible, show the system-provided badge with or without text; never include a playback button that looks like a video play button.
  - Keep badge placement consistent, typically in a corner.
- **Platform notes:**
  - visionOS: people can view a Live Photo but can't capture one.
  - No additional considerations for iOS, iPadOS, macOS, or tvOS. Not supported in watchOS.
- **Copy/labels:** Use the system badge (with "Live" text or without); no video-style play button.
- **APIs:** PHLivePhoto (PhotoKit), LivePhotosKit JS.
- **Web translation:** Use LivePhotosKit JS to play Live Photos on the web, show the standard badge, fall back to the still image where unsupported, and never present a video play control. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/live-photos.md)

### Mac Catalyst
- **Summary:** When you use Mac Catalyst to create a Mac version of your iPad app, you give people the opportunity to enjoy the experience in a new environment.
- **Platforms:** ipados, macos
- **When this applies:**
  - Bringing an iPad app to macOS; strong candidates already support drag and drop, keyboard navigation and shortcuts, multitasking, and multiple windows.
  - Apps whose essential features need gyroscope, accelerometer, rear camera, HealthKit, ARKit, marking, handwriting, or navigation may not suit the Mac.
  - Choosing the iPad or Mac idiom and adapting navigation, layout, inputs, menus, and the app icon.
- **Rules:**
  - You get automatic macOS features: pointer interactions and keyboard focus, window management, toolbars, rich text interaction, file management, menu bar menus, app settings in the system Settings app; split view, file browser, activity view, form sheet, contextual actions, and color picker take on a Mac appearance.
  - Idiom: the default iPad idiom ("Scale Interface to Match iPad") scales views and text to 77% in macOS (17pt text becomes 13pt). Consider the Mac idiom for more detail, Mac-like elements, and better performance, especially for text-heavy, detailed artwork, or animated apps. When you adopt the Mac idiom, thoroughly audit your app's layout and plan changes (consider a separate asset catalog). Adjust font sizes as needed (text renders at 100%); use text styles rather than fixed sizes. Make sure views and images look good at 100% scale. Limit your appearance customizations to standard macOS appearance customizations that are the same or similar to iPadOS.
  - Navigation: replace a tab bar with a split view and sidebar (preferred) or a segmented control (flat hierarchies). Make sure people retain access to important tab-bar items by listing them in the macOS View menu. Offer multiple ways to move between pages (Next and Previous buttons in addition to swipes).
  - Inputs: gestures convert automatically; tap becomes left or right click (mouse) or click (trackpad); touch and hold becomes click and hold; pan becomes left click and drag or click and drag; pinch and rotate map to trackpad pinch and rotate. The two touches in pinch and rotate go to the view under the pointer.
  - App icons: create a macOS version of your app icon with the lifelike macOS rendering style.
  - Layout: divide a single column into multiple columns; use regular-width and regular-height size classes and reflow side by side as the window resizes; present an inspector next to content instead of a popover. Consider moving controls from the main UI to the Mac toolbar and list their commands in menu bar menus. As much as possible, adopt a top-down flow (important actions near the top; iPad toolbar controls go in the window toolbar). Relocate buttons from the side and bottom edges of the screen, which exist for reach on iPad.
  - Menus: Mac users expect all commands in the menu bar; pop-up and pull-down button menus take on a macOS appearance automatically; context menus convert automatically, and you should look for additional places to support them because Mac users expect every object to have one (called a contextual menu on Mac).
- **Platform notes:**
  - No additional considerations for iPadOS or macOS. Not supported in iOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Menu bar command names should mirror the controls they duplicate; list top-level sections in the View menu.
- **APIs:** Mac Catalyst (UIKit), UIKeyCommand, UIMenuBuilder, UICommand, Choosing a user interface idiom for your Mac app, UIKit Catalog, Split views, Tab bars, Page controls, Pop-up buttons, Pull-down buttons.
- **Web translation:** When adapting a touch-first web layout to desktop, replace bottom tabs with a sidebar, move edge-anchored buttons into a top toolbar, add keyboard shortcuts and context menus, and use multi-column layouts at wide breakpoints. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/mac-catalyst.md)

### Machine learning
- **Summary:** Machine learning enables apps and games to learn from data and usage patterns, letting you improve existing experiences and create engaging new ones.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any model-driven feature: recommendations, personalization, recognition, prediction, suggestions.
  - Designing how the feature collects feedback (explicit, implicit, calibration) and how it presents results (multiple options, confidence, attribution, limitations, corrections, mistakes).
- **Rules:**
  - Define the role of machine learning in your app along five axes: critical or complementary (central features need more accuracy); private or public (sensitive data means serious consequences for errors; always protect privacy); proactive or reactive (proactive results must be higher quality because people didn't ask); visible or invisible (invisible features struggle to communicate reliability); dynamic or static (dynamic features often use calibration and feedback).
  - Explicit feedback: request explicit feedback only when necessary; prefer implicit feedback. Always make providing explicit feedback a voluntary task. Use simple, direct language to describe each explicit feedback option and its consequences; avoid imprecise terms like dislike; use options like "Suggest less pop music", "Suggest more thrillers", "Mute politics for a week". Add icons to an option description if it helps, never icons alone. Consider offering multiple options that become progressively more specific. Act immediately when you receive explicit feedback and persist the resulting changes. Consider using explicit feedback to help improve when and where you show results.
  - Implicit feedback (favoriting and social feedback count as implicit): always secure people's information. Help people control their information; explain how your app gets and shares it and let people restrict it. Don't let implicit feedback decrease people's opportunities to explore. When possible, use multiple feedback signals to improve suggestions and mitigate mistakes. Consider withholding private or sensitive suggestions (shared devices). Prioritize recent feedback, falling back to historical. Use feedback to update predictions on a cadence that matches the person's mental model (typing suggestions update instantly; song recommendations shouldn't churn continuously). Be prepared for changes in implicit feedback when you make changes to your app's UI. Beware of confirmation bias; don't rely solely on implicit feedback.
  - Calibration (only when the feature can't function without initial information): always secure people's information. Be clear about why you need people's information, emphasizing what the feature does rather than how it works. Collect only the most essential information. Avoid asking people to participate in calibration more than once, and do it early (exception: calibrating with an object like a baseball field). Make calibration quick and easy: prioritize a few important pieces of information, avoid data people must look up, avoid difficult actions. Make sure people know how to perform calibration successfully with an explicit goal and progress (Face ID tick marks). Immediately provide assistance if progress stalls without implying fault and never without a next step. Confirm success with a clear path to the feature. Let people cancel calibration at any time without judgment. Give people a way to update or remove information they provided during calibration, including outside the calibration flow.
  - Mistakes: understand the significance of a mistake's consequences (wrong keyboard suggestion versus a missed flight) and match corrective tools. Make it easy for people to correct frequent or predictable mistakes. Continuously update your feature to reflect evolving interests and domain information. When possible, address mistakes without complicating the UI (a wrong attribution magnifies a mistake). Be especially careful to avoid mistakes in proactive features. As you work on reducing mistakes in one area, always consider the effect on other areas and overall accuracy.
  - Corrections: give people familiar, easy ways to make corrections (show the controls the automation used, as Photos does for auto-crop). Provide immediate value when people make a correction and persist it. Let people correct their corrections. Always balance the benefits of a feature with the effort required to make a correction. Never rely on corrections to make up for low-quality results. Learn from corrections when it makes sense. When possible, use guided corrections (a list of alternatives) instead of freeform corrections, or combine them.
  - Multiple options (suggested, requested, or corrections): prefer diverse options (Maps offers no-toll, scenic, highway routes). In general, avoid providing too many options; fit them on one screen. List the most likely option first, using confidence or context, and consider selecting it by default. Make options easy to distinguish and choose with brief descriptions and highlighted differences; group large sets into scannable categories. Learn from selections when it makes sense.
  - Confidence: verify that confidence values correspond to result quality before conveying them. Know what your confidence values mean before you decide how to present them. In general, translate confidence values into concepts that people already understand ("Because you listen to pop music" rather than "97% match"). In situations where attributions aren't helpful, consider ranking or ordering results, or use semantic categories like "high chance" and "low chance". In scenarios where people expect statistical or numerical information (weather, sports, polling), display confidence values. Whenever possible, help people make decisions by conveying confidence in terms of actionable suggestions ("This is a good time to buy", "Consider waiting for a better price"). Consider changing how you present results based on different confidence thresholds (Photos asks for confirmation at lower face-recognition confidence). When you know confidence values correspond to result quality, avoid showing results when confidence is low; set a threshold for proactive suggestions.
  - Attribution (the rationale for a result, like "Because you've read mysteries"): consider using attributions to help people distinguish among results ("New books by authors you've read"). Avoid being too specific or too general. Keep attributions factual and based on objective analysis ("Because you've read nonfiction", not "Because you love nonfiction"). In general, avoid technical or statistical jargon except for inherently statistical results.
  - Limitations: help people establish realistic expectations before they use a feature when a limitation is serious but rare. Demonstrate how to get the best results (placeholder text like "Photos, People, Places..."; live feedback like Memoji lighting hints; suggest alternatives instead of showing no results). Explain how limitations can cause unsatisfactory results (Memoji says it doesn't work well in the dark). Consider telling people when limitations are resolved.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Feedback options name the consequence ("Suggest less pop music", "Mute politics for a week"); attributions are factual ("Because you've read nonfiction"); confidence is phrased as actionable suggestions or categories, not raw percentages, unless the domain is statistical.
- **APIs:** Create ML, Core ML, Apple Intelligence and machine learning overview, Generative AI guidance, Privacy foundations.
- **Web translation:** Make feedback voluntary and consequence-labeled, apply it instantly and persistently, show a few diverse ranked options with plain-language reasons, hide low-confidence proactive suggestions, and provide guided corrections for predictable errors. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/machine-learning.md)

### Maps
- **Summary:** A map displays outdoor or indoor geographical data in your app or on your website.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any embedded map (MapKit or MapKit JS): store locators, routing, annotations, overlays.
  - Place cards inside or outside a map.
  - Indoor venue maps and static maps on Apple Watch.
- **Rules:**
  - In general, make your map interactive (zoom, pan, rotate); noninteractive elements that obscure the map break expectations.
  - Pick a map emphasis style: default (fully saturated, aligns with the Maps app) or muted (desaturated, lets information-rich content stand out).
  - Help people find places in your map with search combined with category filters.
  - Clearly identify elements that people select with an outline and color variation.
  - Cluster overlapping points of interest; clusters expand as people zoom in.
  - Help people see the Apple logo and legal link: don't cover them permanently; use adequate padding (about 7 points on the sides and 10 points above and below); keep them fixed to the map rather than moving with your interface; if a custom card moves, place the logo and link 10 points above its lowest resting position. The logo and link aren't shown on maps smaller than 200x100 pixels.
  - Custom information: use annotations that match the visual style of your app (default marker is red with a white pin; you can change tint and icon to a string or image; keep icon strings to two to three characters). If you want to display custom information that's related to standard map features, consider making them independently selectable. Use overlays to define map areas: above roads (default; below buildings and trees) or above labels (hides everything beneath). Make sure there's enough contrast between custom controls and the map (thin stroke, light drop shadow, blend modes).
  - Place cards: styles are automatic, callout (full or compact; automatic callout picks by view size), caption (an "Open in Apple Maps" link), and sheet. Full callouts appear as a popover on iPadOS and macOS and as a sheet on iOS. Consider your map presentation when choosing a style (compact callout for small maps with many annotations). Make sure your place card looks great on different devices and window sizes (set a minimum width for full callouts). Avoid duplicating information your app already shows. Keep the location on your map visible when displaying a place card (use an offset pointing at the location). Outside a map, you must include a map in the place card. Use location-related cues in surrounding content (place names, addresses, a details button, a map pin icon) to signal that a place card can open.
  - Indoor maps: adjust map detail based on the zoom level (rooms and buildings always; stores and restrooms when zoomed in). Use distinctive styling (color plus icons) to differentiate features. Offer a floor picker for multiple levels with concise floor numbers. Include surrounding areas for context, dimmed and distinctly colored if noninteractive. Consider supporting navigation between your venue and nearby transit points, with a way to switch to Apple Maps. Limit scrolling outside of your venue and keep part of the indoor map visible. Design an indoor map that feels like a natural extension of your app; don't replicate Apple Maps.
- **Platform notes:**
  - watchOS: maps are static snapshots placed at design time; tapping opens the Maps app; up to five annotations. Fit the map interface element to the screen without scrolling. Show the smallest region that encompasses the points of interest.
  - No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.
- **Copy/labels:** Annotation icon strings two to three characters; caption-style place cards read "Open in Apple Maps"; floor pickers use numbers rather than names.
- **APIs:** MapKit (MKStandardMapConfiguration.EmphasisStyle, MKAnnotationView, MKMapFeatureOptions, MKOverlayLevel, selection accessories and place card styles, MKMapItemDetailViewController), SwiftUI Map modifiers (`mapItemDetailSelectionAccessory(_:)`, `mapFeatureSelectionAccessory(_:)`, `mapItemDetailSheet(item:displaysMap:)`), MapKit JS (selectionAccessory, PlaceDetail, Maps Embed API), WKInterfaceMap (WatchKit), Indoor Mapping Data Format.
- **Web translation:** MapKit JS is the web path: keep the map interactive, cluster pins, keep the Apple logo and legal link uncovered with the same padding, use place cards or the Maps Embed API for place details, and style annotations to your brand. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/maps.md)

### NFC
- **Summary:** Near-field communication (NFC) allows devices within a few centimeters of each other to exchange information wirelessly.
- **Platforms:** ios, ipados
- **When this applies:**
  - Apps that read NFC tags on real-world objects (toys, store signs, inventory).
  - Writing the text on the in-app scanning sheet and supporting background tag reading.
- **Rules:**
  - Don't encourage people to make contact with physical objects; use "scan" and "hold near" instead of "tap" and "touch".
  - Use approachable terminology; avoid NFC, Core NFC, Near-field communication, and tag. Use "Scan the [object name]." and "Hold your iPhone near the [object name] to learn more about it." instead of "Scan the NFC tag." or "To use NFC scanning, tap your phone to the [object]."
  - Provide succinct instructional text for the scanning sheet: a complete sentence in sentence case with ending punctuation that identifies the object; revise for subsequent scans; keep it short. First scan: "Hold your iPhone near the [object name] to learn more about it." Subsequent scans: "Now hold your iPhone near another [object name]."
  - Background tag reading (system scans whenever the screen is on and shows a notification) isn't available when a scanning sheet is visible, Wallet or Apple Pay are in use, cameras are in use, in Airplane Mode, or when the device is locked after a restart.
  - Support both background and in-app tag reading; you must provide an in-app way to scan.
- **Platform notes:**
  - No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** "Scan" and "hold near", never "tap" or "touch"; no "NFC" or "tag" in user-facing text; sheet text is a full sentence with a period.
- **APIs:** Core NFC.
- **Web translation:** With Web NFC where available, use the same friendly "hold your phone near the [object]" wording, never mention NFC or tags to users, and always provide a non-NFC path. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/nfc.md)

### Photo editing
- **Summary:** Photo-editing extensions let people modify photos and videos within the Photos app by applying filters or making other changes.
- **Platforms:** ios, ipados, macos
- **When this applies:**
  - Apps that offer a photo editing extension that appears in Photos' edit mode.
- **Rules:**
  - Edits are saved as new files, preserving originals.
  - Confirm cancellation of edits: ask people to confirm and tell them edits will be lost; skip the confirmation if no edits were made.
  - Don't provide a custom top toolbar; the modal view already has one.
  - Let people preview edits before returning to Photos.
  - Use your app icon for your photo editing extension icon.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, or macOS. Not supported in tvOS, visionOS, or watchOS.
- **Copy/labels:** The cancel confirmation states that any edits will be lost.
- **APIs:** PhotoKit, App extensions.
- **Web translation:** In a web editor, confirm discarding unsaved edits only when edits exist, show a live preview, and don't stack a second toolbar inside a host's modal. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/photo-editing.md)

### ResearchKit
- **Summary:** A research app lets people everywhere participate in important medical research studies.
- **Platforms:** ios, ipados
- **When this applies:**
  - Apps that enroll participants in a medical study: introduction, eligibility, informed consent, data permissions, surveys, active tasks, profile, and progress.
  - These guidelines are informational, not legal advice.
- **Rules:**
  - Always display the onboarding screens in the correct order: Introduction, Eligibility, Informed consent, Permission to access data.
  - Provide an introduction that informs and provides a call to action; let existing participants log in quickly.
  - Determine eligibility as soon as possible; present only necessary requirements in simple language with easy entry.
  - Make sure participants understand your study before you get their consent; comply with App Store Guidelines and review board requirements.
  - Break a long consent form into easily digestible sections (data gathering, data use, benefits, risks, time commitment, how to withdraw) with a Learn More button for detail; participants must be able to view the entire consent form before agreeing.
  - If it makes sense, provide a quiz that tests the participant's understanding.
  - Get the participant's consent and, if appropriate, some contact information (confirmation dialog, signature, contact details; most apps email a PDF of the consent).
  - Get permission to access the participant's device or data, and to send notifications; explain why and don't request data that isn't critical.
  - Create surveys that keep participants engaged: tell participants how many questions there are and about how long the survey will take; use one screen per question; show progress; keep the survey as short as possible (several short surveys beat one long one); use the standard font for the question and a slightly smaller font for explanatory text; tell participants when the survey is complete.
  - Make active tasks easy to understand: describe how to perform the task in clear, simple language; explain requirements (time, circumstances); make sure participants can tell when the task is complete.
  - Use a profile to help participants manage personal data (edit changing data like weight or sleep, see upcoming activities, leave the study, view the consent document and privacy policy).
  - Use a dashboard to show progress and motivate participants (daily progress, weekly assessments, activity results, comparisons with aggregated results). Keep both screens accessible at all times.
- **Platform notes:**
  - No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Consent sections use simple high-level language with a "Learn More" button; surveys state question count and duration up front.
- **APIs:** ResearchKit (GitHub project), HealthKit Protecting user privacy, CareKit.
- **Web translation:** For a web study, enforce the same order (intro, eligibility, consent in sections with full-text access, permissions), one question per screen with progress, and a persistent profile and progress page. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/researchkit.md)

### SharePlay
- **Summary:** SharePlay lets people experience activities together from anywhere, whether they're watching a movie, playing a game, or sketching on a whiteboard.
- **Platforms:** ios, ipados, macos, tvos, visionos
- **When this applies:**
  - Real-time shared activities synchronized across devices alongside FaceTime or Messages (watching, browsing, games, whiteboards).
  - Starting, joining, and describing activities; handling purchased or subscription content (each participant needs their own access).
  - visionOS shared context, Personas, and spatial templates.
- **Rules:**
  - Use SharePlay for real-time experiences; for asynchronous collaboration, let people share or save the activity afterward (Freeform shares a link).
  - Design an experience that best fits what people are doing together (one shared view for watching or browsing; role-based views for games).
  - Design activities that work across Apple platforms, devices, and communication methods.
  - Make it easy to start a shared activity with a clear control, such as a button with the SharePlay symbol; the share sheet and (in visionOS) the Share button next to the window bar also start activities.
  - Let people join an activity without friction: get them to the content quickly; sign-in, download, or subscribe flows dismiss as soon as done; lower barriers with provisional access or Family Sharing; defer nonessential steps (profiles after joining a match).
  - Describe activities clearly and concisely (title, short summary, poster) without truncation.
  - Keep people oriented as an activity changes: the system coordinates media playback; for other changes, show who's doing what (Freeform shows initials next to contributions).
- **Platform notes:**
  - iOS, iPadOS, macOS: support Picture in Picture for shared video so people keep watching while doing other things (a window they bring forward on Mac).
  - tvOS: no additional considerations. Not supported in watchOS.
  - visionOS: standard windows share via screen mirroring by default; adopt SharePlay for volumes and immersive content. The system creates a shared context so everyone sees content in the same relative location; align windows and volumes across devices. Prefer starting your experience from a window (an immersive start needs custom UI). Resolve conflicts naturally; avoid UI for taking control, let people speak or gesture, consider last change wins. Reserve unique views for moments that call for them; replace a person's spatial Persona with a contact photo when they enter their own immersive view and keep FaceTime Audio going. Let people opt in to immersion changes when they're mid-task (prompt with a join option). Let participants customize their experience for personal comfort and accessibility (volume, subtitles) without affecting others. Make it easy to leave and rejoin. Personas: remote Vision Pro participants appear as spatial Personas or a contact photo; other devices appear in a 2D video window; co-located wearers see each other through passthrough. Support people who aren't represented by a spatial Persona; offer UI alternatives to facial expressions or gestures. Spatial templates: side-by-side (viewing content together, less nonverbal interaction), surround (tabletop games, centralized content, face to face), conversational (content on the edge, people together while the app plays in the background). Divide a complex activity into stages with a template each. Let people initiate template transitions. Keep template transitions smooth (fade out and in, reorientation cues). Custom templates: account for people who are physically together (templates can't move them; use position markers). Provide the best seat orientation for your content. Support the maximum number of seats: up to five spatial Personas, so include five seats; define all seats up front, keep a seat after someone leaves, add spectator seats for limited-player games. Place seats at least a meter apart (a too-close Persona becomes a contact photo). Define the order in which people take seats so the arrangement stays balanced. Keep roles independent of seats; reserve a spot only for a role that requires it (host at the head of a table).
- **Copy/labels:** Use "SharePlay" as a noun ("Join SharePlay") or as a verb in an interface action ("SharePlay Movie"); don't pair it with an adjective (no "virtual" or "spatial" SharePlay); never alter it ("SharePlayed", "SharePlays", "SharePlaying").
- **APIs:** Group Activities (SystemCoordinator spatial template preference, SpatialTemplateSeatElement, `isSpatial`, `isNearbyWithLocalParticipant`), Shared with You collaboration, Presenting SharePlay activities from your app's UI, Implementing SharePlay for immersive spaces in visionOS.
- **Web translation:** n/a for SharePlay itself; a web watch-together feature should still sync playback, show who did what, let people join with one click, and keep personal settings (volume, captions) local. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/shareplay.md)

### ShazamKit
- **Summary:** ShazamKit supports audio recognition by matching an audio sample against the ShazamKit catalog or a custom audio catalog.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Features that react to currently playing music, sync captions or sign language to audio, or sync in-app experiences to external content.
  - Requesting microphone access and storing recognized songs.
- **Rules:**
  - If you need the microphone, request access and explain why (example purpose: "Synchronize reading and math exercises with videos played by your teacher.").
  - Stop recording as soon as possible; record only long enough to get the sample.
  - Let people opt in to storing your app's recognized songs to their iCloud library.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** A clear microphone purpose string tied to the feature.
- **APIs:** ShazamKit (catalog and custom catalog matching).
- **Web translation:** Request microphone access only on a user action with a clear reason, stop capture immediately after sampling, and ask before saving anything to a user's library. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/shazamkit.md)

### Sign in with Apple
- **Summary:** Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Any sign-in or account creation flow, on Apple platforms, the web, and non-Apple platforms.
  - Collecting additional data after sign-in, handling private relay email addresses, and linking existing accounts.
  - Displaying system or custom Sign in with Apple buttons.
- **Rules:**
  - Ask people to sign in only in exchange for value, with a brief description of the benefits.
  - Delay sign-in as long as possible.
  - If you require an account, ask people to set it up before offering any sign-in options; explain why, then offer Sign in with Apple and other methods.
  - Consider letting people link an existing account to Sign in with Apple (matching email suggestion; a link option in account settings).
  - In a commerce app, wait until after people make a purchase before asking them to create an account; with Apple Pay, offer account creation on the order confirmation page without re-asking for name and email.
  - As soon as Sign in with Apple completes, welcome people to their new account; don't ask for information that isn't required.
  - Indicate when people are currently signed in with a phrase like "Using Sign in with Apple" in settings or account UI.
  - Collecting data: clarify whether the additional data you request is required (terms, region, birth date, real-identity laws) or just recommended. Don't ask people to supply a password unless they've stopped using Sign in with Apple. Avoid asking for a personal email address when people supply a private relay address; show the relay address in your app, point to Settings > Apple Account > Password & Security > Apps using Apple Account, or use order or phone numbers for identification. Give people a chance to engage with your app before asking for optional data, and don't block features if they decline. Be transparent about the data you collect (welcome people by the name or email they shared).
  - Buttons: prominently display a Sign in with Apple button, no smaller than other sign-in buttons, without scrolling.
  - System buttons give an approved appearance, proportions, automatic translation, corner radius configuration (iOS, macOS, web), and a VoiceOver label. Titles available on iOS, macOS, tvOS, and web: Sign in with Apple, Sign up with Apple, Continue with Apple; watchOS offers only "Sign in". Use one variant consistently.
  - Styles: white (all platforms; dark backgrounds with sufficient contrast), white with outline (iOS, macOS, web; light backgrounds that lack contrast with white; not on dark or saturated backgrounds), black (all platforms; light backgrounds; not on dark). The watchOS button uses system dark gray instead of pure black.
  - Adjust the corner radius to match other buttons (square to capsule) in iOS, macOS, and web.
  - Maintain the minimum button size and margin in iOS, macOS, and web: minimum width 140pt (140px @1x, 280px @2x), minimum height 30pt (30px @1x, 60px @2x), minimum margin 1/10 of the button's height.
  - Custom buttons (iOS, macOS, web; reviewed by App Review): must be instantly identifiable as Sign in with Apple. Use only the Apple logo artwork from Apple Design Resources (PNG, SVG, PDF; black and white); never create a custom Apple logo. Use the logo file to position the logo, never the logo as a button; match the logo file height to the button height; don't crop; don't add vertical padding. Don't change: titles (only Sign in with Apple, Sign up with Apple, Continue with Apple), general shape (logo plus text is rectangular; logo-only can be circular or rectangular), logo and title colors (both black or both white). You may change: title font, weight, and size; title case (all caps allowed); background appearance (stays black or white; subtle texture or gradient allowed); corner radius; bezel stroke and drop shadow.
  - Custom buttons with logo and text: choose the logo file format by button height (SVG and PDF for any height; PNG only for 44 pt tall buttons, the iOS default and recommended height; small, medium, large logo sizes). Prefer the system font for the title; the title's font size is 43% of the button height (button height is 233% of the font size, rounded), for example 44 pt button with 19 pt text, 56 pt button with 24 pt text. In general, preserve the capitalization style (capitalize Sign or Continue and Apple only) unless your interface is all uppercase. Keep the title and logo vertically aligned (center the title, logo height equals button height). Inset the logo if necessary to align with other logos. Maintain a minimum margin between the title and the right edge of at least 8% of the button's width. Maintain the minimum button size and margin: width 140 pt, height 30 pt, margin 1/10 of the height.
  - Custom logo-only buttons: SVG or PDF for any size; PNG only for 44x44 pt. Don't add horizontal padding (always 1:1 with built-in padding). Use a mask to change the default square shape (circle or rounded rectangle); never crop the padding or use the logo alone. Maintain a minimum margin of 1/10 of the button's height.
- **Platform notes:**
  - No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
- **Copy/labels:** Button titles exactly "Sign in with Apple", "Sign up with Apple", or "Continue with Apple" (watchOS: "Sign in"); status text "Using Sign in with Apple"; capitalization: Sign or Continue and Apple capitalized, rest lowercase.
- **APIs:** Authentication Services (ASAuthorizationAppleIDButton, `cornerRadius`), WKInterfaceAuthorizationAppleIDButton (WatchKit), Displaying Sign in with Apple buttons on the web, Sign in with Apple button configurator, Apple Design Resources.
- **Web translation:** Use the official Sign in with Apple JS button (or a compliant custom button with the Apple logo asset, exact titles, black or white only, 140x30 minimum), place it no smaller than other sign-in buttons above the fold, and honor private relay addresses. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/sign-in-with-apple.md)

### Siri
- **Summary:** People use Siri to help them with the things they need to find, know, or do every day.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Exposing app actions (intents) and content (entities) to Siri, Spotlight, and Shortcuts through App Intents and app schemas.
  - Writing Siri response dialogue, follow-up questions, and error responses for custom responses.
  - Referring to Siri in your UI or marketing.
- **Rules:**
  - Make features and content available with the App Intents framework; adopt app schemas for common domains (email, music, photos) to get built-in handling with natural conversation and context.
  - Share contextual information: annotate onscreen views with app entities, donate entities to the Spotlight index, and donate actions as intents so Siri can anticipate future actions.
  - Identify your app's most popular actions, and when and where they occur, to prioritize what you expose.
  - Use familiar terms for your content and actions (track, song, or podcast as people say it).
  - Offer relevant content to Spotlight (recent searches, favorites, bookmarks, wishlists), with broader access for categories like email or messaging.
  - Don't advertise in content Siri delivers; no marketing or in-app purchase pitches.
  - Only provide a custom response if built-in responses don't meet your app's needs.
  - App Shortcuts expose custom actions outside existing schemas; optional intent and entity properties (like a playback snippet) can enhance responses but may not always appear because responses can be nonvisual.
  - Write response dialogue that's clear and descriptive ("Which soup?" rather than "Which one?").
  - Keep responses as succinct as possible; remove details the conversation already covers; avoid humor that grows irritating.
  - Provide responses that Siri can deliver audibly and visually; the voice response must stand alone.
  - Design inclusive interactions; avoid unnecessary pronouns ("Who should I send it to?" instead of "What's his or her name?").
  - Ask an open-ended question when the full list of options is too long ("What kind of shoes are you interested in?").
  - Keep responses device-independent whenever possible.
  - Omit your app name from responses; the system attributes it.
  - Use appropriate language and respect parental controls; no offensive language; responses may be spoken aloud.
  - Help people understand errors and failures with specific responses ("Sorry, we're out of chicken noodle soup" rather than "Sorry, we can't complete your order").
- **Platform notes:**
  - The page lists no platform-specific considerations.
- **Copy/labels:** Refer to Siri by name, never as she, him, or her. Never impersonate Siri, reproduce its functionality, or appear to respond as Apple; don't use reserved phrases like "Call 911" or "Hey Siri". In a localized context, translate only the word "Hey" in "Hey Siri"; "Siri" is never translated (for example es_ES "Oye Siri", fr_FR "Dis Siri", de_DE "Hey Siri", it_IT "Ehi Siri", ja_JP "Hey Siri", ko_KR "Siri야", pt_BR "E aí Siri", ru_RU "привет Siri", zh_CN "嘿Siri", da_DK and sv_SE "Hej Siri", nb_NO "Hei Siri", nl_NL "Hé Siri", ms_MY "Hai Siri", th_TH "หวัดดี Siri", tr_TR "Hey Siri", ar "يا Siri"; full table in the reference).
- **APIs:** App Intents (app entities, intents, App Shortcuts, snippets, app schema domains, Apple Intelligence and Siri AI, donations, Spotlight entities, contextual cues), Snippets component.
- **Web translation:** n/a for Siri integration; the response-writing rules (succinct, device-independent, specific errors, no pronouns) apply well to any web voice assistant or chatbot copy. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/siri.md)

### Tap to Pay on iPhone
- **Summary:** Tap to Pay on iPhone lets merchants accept contactless payments using an app on their iPhone, without having to connect external hardware.
- **Platforms:** ios
- **When this applies:**
  - Merchant payment apps working with a supported payment service provider (PSP) and the Tap to Pay on iPhone entitlement.
  - Terms acceptance, merchant education, checkout flow, result display, and non-payment card reads (lookups, refunds, loyalty).
- **Rules:**
  - Enabling: help merchants accept Tap to Pay on iPhone terms and conditions before they begin interacting with customers (in in-app messaging or onboarding). Present terms and conditions only to an administrative user; tell nonadministrators that administrator access is required; enterprise setups may accept via web or another app. If necessary, help merchants make sure their device is up to date before presenting the terms.
  - Educating: provide a tutorial that describes the supported payment types and shows how to use Tap to Pay on iPhone for each (Learn More in in-app messaging, after accepting terms, for new users, and always in help or settings). Use Apple-approved assets or the ProximityReaderDiscovery API for a localized, maintained tutorial. A custom tutorial must show how to launch checkout per payment type, how a customer positions a contactless card or wallet on the device, and how PIN entry works including accessibility mode, and must end with a chance to accept the terms.
  - Checkout: provide Tap to Pay on iPhone as a checkout option whether the feature is enabled or not; present terms if needed and show the Tap to Pay screen when configuration completes. Avoid making merchants wait; prepare the feature at app start and on every return to the foreground. Make sure the checkout option is available even if configuration is continuing in the background, showing a progress indicator (indeterminate normally; determinate when the API reports progress). If your app supports multiple payment-acceptance methods, make the Tap to Pay on iPhone button easy to find without scrolling; if it's your only method, open it automatically when checkout begins. Make it easy for merchants to switch between Tap to Pay on iPhone and hardware accessories, with setup for both at once and selection in the checkout flow. Design your Tap to Pay on iPhone button to match the other buttons in your app (color and shape are yours; the label is fixed). Determine the final amount that customers need to pay before merchants initiate the Tap to Pay on iPhone experience (tipping first). If you support pre-payment options, display them before the Tap to Pay on iPhone screen.
  - Results: start processing a transaction as soon as possible (request the result before the checkmark animation finishes). Display a progress indicator while payment is authorizing, after the Tap to Pay screen animation finishes, before your result screen. Clearly display the result of a transaction, declined or successful, and offer digital receipts (QR code, text message). Help merchants complete the checkout flow when a payment can't complete with Tap to Pay on iPhone (accept cash, use external hardware or a payment link, or relaunch Tap to Pay for another card). Handle regional cases like Strong Customer Authentication PIN requests and Offline PIN markets with your PSP. If the system returns an error that the merchant must address, display a clear description and a resolution (an alert recommending an iOS update). Make it easy for merchants to get help (in-app help, website, contact support action).
  - Additional interactions: use a generic label in a button that reads a payment card when there's no transaction amount ("Look Up", "Store Card", "Verify", "Refund"), not "Tap to Pay on iPhone" or "Tap to Pay". If your app supports an independent loyalty card transaction, distinguish it with a separate, clearly labeled button ("Loyalty Card", not "Tap to Pay on iPhone - Loyalty") and avoid payment-related terms in its label.
- **Platform notes:**
  - No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS. Works alongside existing payment hardware.
- **Copy/labels:** Payment button label "Tap to Pay on iPhone" or, if space is constrained, "Tap to Pay" (reuse Charge or Checkout only if it's your sole method); use the SF Symbols `wave.3.right.circle` or `wave.3.right.circle.fill` if you use icons in payment buttons; never the Apple logo. Non-payment reads use generic labels ("Look Up", "Store Card", "Verify", "Refund"); loyalty flows avoid "Tap to Pay".
- **APIs:** ProximityReader (PaymentCardReader `prepare(using:)`, `Event.updateProgress(_:)`, `Event.readyForTap`, `Options.returnReadResultImmediately`, PaymentCardReaderSession.ReadError, ProximityReaderDiscovery), Progress indicators, Alerts, SF Symbols.
- **Web translation:** n/a (requires iPhone hardware).
- **Source:** [reference](../references/technologies/tap-to-pay-on-iphone.md)

### VoiceOver
- **Summary:** VoiceOver is a screen reader that lets people experience your app's interface without needing to see the screen.
- **Platforms:** ios, ipados, macos, tvos, visionos, watchos
- **When this applies:**
  - Every app and game (including Unity games via Apple's Unity plug-ins): labels, image descriptions, charts, titles, grouping, change announcements, rotor support.
  - visionOS apps that define custom gestures.
- **Rules:**
  - Provide alternative labels for all key interface elements; system controls have generic labels by default, so give more descriptive ones and label every custom element; keep them current.
  - Describe meaningful images, conveying only what the image itself conveys (not nearby captions).
  - Make charts and other infographics fully accessible with a concise description and accessible versions of any interactions.
  - Exclude purely decorative images from VoiceOver.
  - Use titles and headings to help people navigate your information hierarchy; unique page titles and accurate section headings.
  - Specify how elements are grouped, ordered, or linked when relationships are only visual (group an image with its caption so VoiceOver reads them together; reading order follows the locale, top-to-bottom, left-to-right in US English).
  - Inform VoiceOver when visible content or layout changes occur.
  - Support the VoiceOver rotor when possible by identifying headings, links, and other content types.
- **Platform notes:**
  - visionOS: be mindful that custom gestures aren't always accessible; with VoiceOver on, apps don't receive hand input by default unless the person enables Direct Gesture mode.
  - No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.
- **Copy/labels:** Accessibility labels describe function, not generic control type; page titles are unique and succinct.
- **APIs:** SwiftUI Accessibility modifiers (`accessibilityHidden(_:)`, AccessibilityRotorEntry), UIKit (`isAccessibilityElement`, UIAccessibilityCustomRotor, Supporting VoiceOver in your app), AppKit (`accessibilityElement`, NSAccessibilityCustomRotor), `shouldGroupAccessibilityChildren`, AccessibilityNotification, Apple's Unity plug-ins.
- **Web translation:** Provide meaningful `alt` text and empty `alt` for decorative images, use semantic headings and landmarks, group related content in a single accessible element, announce dynamic changes with `aria-live`, and give charts a text summary plus accessible data. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/voiceover.md)

### Wallet
- **Summary:** Wallet helps people securely store their credit and debit cards, driver's license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.
- **Platforms:** ios, ipados, macos, visionos, watchos
- **When this applies:**
  - Issuing passes (boarding passes, coupons, event tickets, store cards, generic and poster generic passes) and keeping them updated.
  - Order tracking for purchases made in your app or website.
  - Identity verification with the Verify with Wallet button.
- **Rules:**
  - Passes: offer to add new passes to Wallet with system UI (one tap), in the background after one-time authorization for predictable actions like flight check-in, or via a custom view with an Add to Apple Wallet button. Help people add a pass created outside your app on next open; if they decline, don't ask again. Add related passes as a group (multi-connection boarding passes; bundled event tickets). Display an Add to Apple Wallet button to let people add an existing pass not already in Wallet wherever the pass information appears. Let people jump from your app to their pass in Wallet with a link like "View in Wallet". Tell the system when your passes expire (expiration date, relevant date, voided). Always get permission before deleting passes from Wallet (a setting for manual versus automatic removal, or an alert). Help the system suggest a pass when relevant (time and place; Lock Screen link; Live Activity for event tickets). Keep passes up to date (gate changes, delays). Use change messages only for updates to time-critical information, never for marketing.
  - Anatomy: pass fields (logo and logo text, header fields visible when collapsed, primary field, secondary and auxiliary fields, footer fields such as "Family" or "Annual", back fields) plus semantic tags, which are required for poster event and semantic boarding passes and enable automatic layout and featured actions; include pass fields too for older iOS. Supplemental information can live in sheets linked from the front; the back holds rarely needed settings and legal text.
  - Designing passes (use Pass Designer): design a pass that looks great and works well on all devices; don't put essential information in elements unavailable on some devices; avoid padding in images (watchOS crops white space). Keep the pass front uncluttered; essential information in the header; details on the additional information sheet. Make your pass instantly identifiable with brand colors and imagery. Ensure sufficient contrast between background and text colors on solid and image backgrounds. Use language that works on any device ("Slide to view" doesn't apply on Apple Watch).
  - Pass styles: boarding passes (airline passes use semantic tags; other transit uses pass fields), coupons, event tickets (poster style with full-art background via semantic tags; non-poster with background image and thumbnail), store cards (show balance), poster generic passes (full background, flexible), generic passes (gym card, coat check).
  - Pass images (PNG, @2x and @3x): reserve pass images for visual content; no embedded text or barcodes (use fields, tags, and barcode APIs). Keep image file sizes small. Provide a pass icon (app icon or separate). Logo: logo.png, min width 50 pt, max width 160 pt, height 50 pt (non-semantic boarding, non-airline boarding, coupons, non-poster event tickets, generic, store cards); avoid inner drop shadows on logo artwork. Primary logo: primaryLogo.png, min width 30 pt, max width 126 pt, height 30 pt (airline boarding, poster event, poster generic). Secondary logo: secondaryLogo.png, min width 12 pt, max width 135 pt, height 12 pt (poster event ticket, bottom-trailing). Icon: icon.png, 38x38 pt, all styles, system rounds corners. Strip image: strip.png, 375x144 pt (coupon, store card); text can overlay it, so keep areas behind text uncluttered and put key visuals toward the bottom or trailing edge. Thumbnail: thumbnail.png, min width 60 pt, max width 90 pt, height 90 pt, square with rounded corners, transparent PNG (event ticket, generic). Background: background.png 343x503 pt for non-poster event tickets (blurred); artwork.png 358x448 pt for poster event tickets and poster generic passes (unblurred); keep content in the safe area because a material strip covers the bottom edge and account for the barcode. Footer: footer.png, 268x15 pt, airline boarding passes only.
  - Order tracking: make it easy for people to add an order to Wallet (automatically after Apple Pay via PKPaymentOrderDetails or ApplePayPaymentOrderDetails; the system Track with Apple Wallet button via AddOrderToWalletButton on confirmation, status, tracking pages, and emails). Make information about an order available immediately after people place it, with a status description like "Check back later for full order details." if details are pending. Provide fulfillment information as soon as it's available and keep status up to date (Order Placed, Processing, Ready for Pickup, Picked Up, Out for Delivery, Delivered, Issue, Canceled). Supply a high-resolution logo image with a nontransparent background, PNG or JPEG, 300x300 pixels. Supply distinct, high-resolution product images with nontransparent backgrounds, PNG or JPEG, 300x300 pixels, straightforward depictions. In general, keep text brief. Use clear, approachable language, localize it, and match the final confirmed price. Provide a universal link to where people manage their order. Clearly describe each item with line items (price, name, image; optional PDF receipt per transaction). Supply a prioritized list of your apps so the system links the right installed app. Avoid sending duplicate notifications when your app is installed. Make it easy for customers to contact the merchant (at minimum a website link; also Messages for Business, phone, email, support page). Help people track their order: carrier link plus tracking number, a scannable pickup barcode, and clear receiving or pickup instructions. Keep the fulfillment screen centered on order tracking. Choose shipping-fulfillment values that match your details (carrier name or default "Track Shipment"; `onTheWay`, `outForDelivery`, `delivered` when known, otherwise `shipped`; always a tracking link when available). Keep customers informed through relevant fulfillment status descriptions. Be direct and thorough when describing an Issue or Canceled status.
  - Identity verification (iOS 16 and later; Apple never sees the ID documents, you receive encrypted data): present a Wallet verification option only when the device supports it and provide a fallback method. Ask for identity information only at the precise moment you need it, not at account creation. Clearly and succinctly describe the reason you need the information in a purpose string shown on the verification sheet, for example "Federal law requires this information to verify your identity and also to help [App Name] prevent fraud." or "Applicable state law requires [App Name] to verify your driving privileges."; one brief, complete, direct sentence in sentence case, active voice, ending with a period. Ask only for the data you actually need (age threshold via `age(atLeast:)` rather than birth date). Clearly indicate whether you will keep the data and for how long (PKIdentityIntentToStore drives system explanatory text). Choose the system-provided verification button that matches your use case: Verify Age with Apple Wallet (transaction completes after an age check, like leasing a car), Verify Identity with Apple Wallet (transaction completes after identity verification, like a car rental), Continue with Apple Wallet (verification is one part of a longer process needing more data, like opening a financial account), Verify with Apple Wallet (verification completes the flow but the other labels don't fit, like a government service). Buttons are white text on black, optionally with a light outline for dark backgrounds, with adjustable corner radius; multiline variants appear automatically when space is constrained.
- **Platform notes:**
  - watchOS: passes appear in a scrolling carousel; people can add your pass even without a watch app. Tapping a pass reveals a scrolling details screen. Layout rows: logo plus essential field, primary field, secondary and auxiliary fields; overflow goes to the details screen. watchOS crops the strip image to the card aspect ratio and may crop white space from other images. Boarding: logo and departure or boarding time, origin and destination, passenger and seat. Coupon: logo and expiration, strip image. Store: logo, strip image, member name and number. Event: logo and start date, event info, attendee and seat. Generic: logo and expiration, strip image, name and number.
  - No additional considerations for iOS, iPadOS, macOS, or visionOS. Not supported in tvOS.
- **Copy/labels:** "Add to Apple Wallet" button and badge; link text like "View in Wallet"; "Track with Apple Wallet" system button; default carrier label "Track Shipment"; pending status "Check back later for full order details."; identity purpose strings are single sentences in sentence case ending with a period; verification buttons read Verify Age with Apple Wallet, Verify Identity with Apple Wallet, Continue with Apple Wallet, Verify with Apple Wallet.
- **APIs:** PassKit (PKPassLibrary `addPasses(_:withCompletionHandler:)`, `Capability.backgroundAddPasses`, PKAddPassesViewController, PKAddPassButton, PKPaymentOrderDetails, VerifyIdentityWithWalletButton, PKIdentityButton.Label, PKIdentityButton.Style.blackOutline, `cornerRadius`, PKIdentityElement `age(atLeast:)`, PKIdentityIntentToStore), Wallet Passes (Pass, semantic tags, `footerBackgroundColor`, web service for updates), Wallet Orders (Order, LineItem, Merchant, ShippingFulfillment), FinanceKit and FinanceKitUI (AddOrderToWalletButton), ApplePayPaymentOrderDetails (web), Pass Designer, universal links.
- **Web translation:** Distribute .pkpass files with the official Add to Apple Wallet badge, bundle related passes, add the Track with Apple Wallet button to confirmation and tracking pages and emails, keep order status current, and request identity data only at the step that requires it. (Translation, not Apple guidance.)
- **Source:** [reference](../references/technologies/wallet.md)
