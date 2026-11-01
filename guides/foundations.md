# Foundations: the rules that apply to every screen

Condensed from Apple's eighteen Foundations pages. Each section lists Apple's rules as imperatives, keeps Apple's numbers,
and links the full page. Read the full page whenever a rule needs its examples or exceptions. For exact values see
[design-tokens.md](design-tokens.md).

## Accessibility ([reference](../references/foundations/accessibility.md))

An accessible interface is intuitive, perceivable, and adaptable. Audit with Accessibility Inspector. Treat accessibility as a requirement from day one, not a late pass.

Vision
- Support larger text sizes; let people enlarge text at least 200 percent (140 percent in watchOS), ideally through Dynamic Type.
- Use the recommended default and minimum type sizes per platform (17/11 iOS and iPadOS, 13/10 macOS, 29/23 tvOS, 17/12 visionOS, 16/12 watchOS).
- Heavier weights read better at small sizes; thin custom fonts need larger sizes.
- Meet 4.5:1 contrast for text up to 17 pt, 3:1 at 18 pt and for bold text. If you cannot by default, provide a higher-contrast scheme when Increase Contrast is on. Check both light and dark.
- Prefer system colors; they have accessible variants built in.
- Never rely on color alone; add shapes, icons, or text.
- Label everything for VoiceOver; see [VoiceOver](../references/technologies/voiceover.md).

Hearing
- Provide captions, subtitles, audio descriptions, or transcripts as appropriate; never communicate essential information through audio alone.
- Pair audio cues with haptics and with visual cues (especially in games and spatial apps where events happen off screen).

Mobility
- Meet the minimum control sizes (44 pt iOS and iPadOS and watchOS, 28 pt macOS, 66 pt tvOS, 60 pt visionOS) and give controls about 12 pt (bezeled) or 24 pt (bezel-less) of surrounding padding.
- Prefer simple gestures; offer an alternative to every gesture; never make a gesture the only way to do something important.
- Support Voice Control, Siri and Shortcuts, VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control, Switch Control.
- Let people do everything with the keyboard alone where a keyboard exists.

Cognitive
- Keep actions simple, consistent, and predictable; prefer system gestures and components.
- Minimize UI that auto-dismisses on a timer.
- Games: offer difficulty accommodations.
- Let people control audio and video playback; never autoplay without controls.
- Let people opt out of flashing lights; be cautious with fast or blinking animation; honor Reduce Motion.
- iOS and iPadOS: optimize for Assistive Access (large, simple, focused UI).

visionOS
- Support Pointer Control (hand and head), Zoom, and Dwell Control; never anchor content to the wearer's head; prioritize comfort.

## App icons ([reference](../references/foundations/app-icons.md))

- Layered icon: background plus one or more foreground layers; build it in Icon Composer (iOS, iPadOS, macOS, watchOS) or an Xcode image stack (tvOS 2 to 5 layers, visionOS 1 to 2 layers over a background).
- Canvas 1024x1024 px (watchOS 1088, tvOS 800x480). Supply square unmasked layers; the system masks to rounded square (iOS, iPadOS, macOS), rounded rectangle (tvOS), or circle (visionOS, watchOS). Keep key content centered.
- Prefer vector layers (SVG, PDF), outlined text, PNG only for raster and mesh gradients. Crisp edges, varied opacity for depth, a background that emphasizes the foreground.
- Let the system add highlights, shadows, blur, and specular effects. Do not bake them in.
- One concept, simple shapes, no UI replicas, no photos, text only if essential to the brand, no Apple hardware.
- Consistent design across every platform you ship on.
- Provide default, dark, clear, and tinted appearances (iOS, iPadOS, macOS) with the same core features; base dark on light with complementary colors; alternate icons need their own variants too.
- tvOS: keep a safe zone for focus scaling. visionOS: no fake holes in the background. watchOS: no black background.

## Branding ([reference](../references/foundations/branding.md))

- Express brand through voice and tone, accent color used sparingly for primary actions and status, optional custom font for headlines (must support Dynamic Type and Bold Text), and familiar components.
- Branding always defers to content. No logos sprinkled through the UI. The launch screen is not a branding moment.
- Keep standard patterns and placements so even a stylized app feels approachable.
- Follow Apple's trademark guidelines; no Apple trademarks in the app name or images.

## Color ([reference](../references/foundations/color.md))

- One meaning per color, applied consistently (interactive versus decorative especially).
- Every color must work in light, dark, and Increase Contrast. Custom colors need light and dark variants plus increased-contrast options.
- Test under different lighting, True Tone, and devices; consider how artwork and translucency shift nearby colors.
- Prefer the system color picker when people choose colors.
- Never rely on color alone; mind cultural meanings.
- Do not hard-code system color values; use the semantic APIs. Do not repurpose semantic colors.
- Liquid Glass has no inherent color. Apply color sparingly on it: tint the background of the single primary action (prominent button), keep symbols and text monochrome, prefer monochrome bars over colorful content, keep the resting state of scrolling content legible beneath controls.
- Use sRGB by default; use Display P3 (16-bit PNG) for richer media; provide per-gamut variants when P3 colors clip or merge on sRGB.
- iOS and iPadOS: system and grouped background sets (primary, secondary, tertiary); label, secondaryLabel, tertiaryLabel, quaternaryLabel, placeholderText, separator, opaqueSeparator, link.
- macOS: the full set of NSColor semantic colors (labelColor, controlAccentColor, windowBackgroundColor, selectedContentBackgroundColor, and so on); the person's chosen accent overrides yours unless the setting is multicolor.
- tvOS: limited palette aligned to the logo; focus is shown by scale and motion, not color alone.
- visionOS: color sparingly on glass, in bold text and large areas; balance brightness in immersive scenes.
- watchOS: background color only when it communicates; graphic complications may be tinted.

## Dark Mode ([reference](../references/foundations/dark-mode.md))

- Never offer an app-specific appearance setting. Look good in light, dark, and Auto.
- Use semantic, adaptive colors; add custom colors as Color Sets with both variants.
- Contrast at least 4.5:1, aim for 7:1 for custom pairs.
- Soften white image backgrounds; design separate light and dark icons or images when one asset does not work in both.
- Use SF Symbols; they adapt automatically.
- Test with Increase Contrast and Reduce Transparency, separately and together.
- A permanently dark UI is acceptable only for immersive media apps.

## Icons (interface icons) ([reference](../references/foundations/icons.md))

- Simple, recognizable, familiar metaphors; consistent size, detail, stroke weight, and perspective across the app.
- Match icon weight to adjacent text weight. Optically center asymmetric icons by adding padding.
- No separate selected-state assets for standard components; the system handles selection.
- Inclusive imagery; text only when essential, and localized.
- Vector (PDF or SVG); alternative text labels; no Apple hardware replicas.
- Use the standard SF Symbols for common actions (see design-tokens.md for the full list: `square.and.arrow.up` Share, `trash` Delete, `plus` Add, `ellipsis` More, `magnifyingglass` Search, and so on).
- macOS document icons: folded-corner shape, background fill plus optional center image and term; sizes listed in design-tokens.md.

## Images ([reference](../references/foundations/images.md))

- Provide every scale factor the platform needs (iOS @2x @3x; iPadOS and watchOS @2x; macOS and tvOS @1x @2x; visionOS @2x or higher). Design at 1x and scale up.
- Embed color profiles; test on real devices.
- Layered images (tvOS, visionOS): standard elements, clear foreground, middle, background layers, text in front, opaque background, simple layering, safe zone, always preview.
- Prefer vector for 2D art; balance resolution and performance for raster; avoid transparency to keep files small; autoscaling PDFs give one asset for all sizes.
- visionOS spatial photos and scenes: render correctly, feathered glass behind text, standalone views, minimal UI when immersive, centered large scenes.

## Immersive experiences (visionOS) ([reference](../references/foundations/immersive-experiences.md))

- Offer multiple ways to use the app; launch in the Shared Space or the mixed style; reserve full immersion for meaningful moments.
- Keep people comfortable: content within the field of view, no required movement, do not obscure too much passthrough, subtle passthrough tints.
- Smooth predictable transitions; let people choose when to enter or exit; make exit controls unambiguous.
- Virtual hands: natural size and behavior; fade to real hands when tracking drops.
- Environments: minimal distraction, clear interactive objects, subtle animation, expansive scale, ground plane, Spatial Audio, real meshes instead of flat 360 images, varied assets.

## Inclusion ([reference](../references/foundations/inclusion.md))

- Design for everyone from the start: welcoming language (address people as "you", avoid "the user"), define technical terms, plain language instead of idioms, be careful with humor.
- Be approachable; represent people of all gender identities, bodies, abilities, and settings; avoid stereotypes in copy, imagery, avatars, and characters.
- People-first language about disability; simplicity and perceivability first.
- Support the languages and scripts people use; see Right to left.

## Layout ([reference](../references/foundations/layout.md))

- Order by importance in reading order; align to scan; indent to show subordination; group with space, containers, or separators; use progressive disclosure.
- Differentiate controls from content with Liquid Glass and scroll edge effects, not solid bar backgrounds; extend full-bleed backgrounds under sidebars, toolbars, tab bars (background extension effect when needed).
- Adapt to size classes, screen sizes, orientation, Dynamic Island, external displays, Display Zoom, resizable windows, text size, and locale. Use SwiftUI or Auto Layout.
- Decide layout from size classes (compact or regular, horizontal and vertical), never from device type or orientation. Consider every combination. Keep functionality the same as size changes; switch tab bar to sidebar or expose overflow items when space grows.
- Respect safe areas and layout guides. Be ready for Dynamic Type: stack horizontally adjacent views, let rows grow, reduce columns.
- Preview at the smallest and largest layouts, every size class, localization, and text size. Scale background art to fill without changing aspect ratio.
- macOS: nothing critical at the window bottom; nothing behind the camera housing.
- tvOS: 60 pt top and bottom, 80 pt sides; padding for focus growth; use the published grid widths.
- visionOS: support resizing with sensible min and max; 3D in windows sparingly; supplemental content in an adjacent window, not an ornament; button centers 60 pt apart.
- watchOS: at most three glyph buttons or two text buttons per row; consider autorotation for views people show others.

## Materials ([reference](../references/foundations/materials.md))

- Two kinds: Liquid Glass (floating controls and navigation layer) and standard materials (content layer).
- Never use Liquid Glass in the content layer, except controls like sliders and toggles that take on glass while active.
- Use glass effects sparingly on custom controls; standard components get it automatically.
- Regular variant by default (alerts, sidebars, popovers, text-heavy components). Clear variant only over rich media, with a 35 percent dark dimming layer when the content behind is bright.
- Choose standard materials by semantic use; use vibrant colors on top; thicker for small text contrast, thinner to preserve context.
- iOS and iPadOS: ultraThin, thin, regular, thick; vibrancy levels for labels, fills, separators; avoid quaternary on thin materials.
- macOS: vibrancy and blending modes for sidebars and content; inactive windows lose vibrancy.
- visionOS: the window glass background is fixed; keep it.

## Motion ([reference](../references/foundations/motion.md))

- Motion must have a purpose and must be optional; provide non-motion alternatives (haptics, text) and honor Reduce Motion.
- Feedback motion follows the gesture realistically, is brief and precise, and can be canceled. Avoid adding motion to frequent interactions beyond the system defaults.
- Animated SF Symbols are a good lightweight option.
- Games: steady 30 to 60 fps; offer power and quality options.
- visionOS: no motion at the edges of view, no world rotation, fades for relocation, stationary frames of reference, no sustained oscillation near 0.2 Hz.

## Privacy ([reference](../references/foundations/privacy.md))

- Request only data you need, only when the feature needs it, never at launch unless the app cannot function without it.
- Be transparent; process on device where possible; adopt system protections (CloudKit encryption, App Sandbox, Developer ID on macOS).
- Purpose strings: explain exactly how the app uses the data, in a short complete sentence, no incentives.
- A pre-alert screen may have exactly one button and that button must open the system alert; no close or skip; no imitation of the system alert; no annotated screenshots of it; never mislead before tracking requests.
- Prefer the location button for one-off location sharing; customize it to fit the UI.
- Passkeys over passwords; Sign in with Apple; store secrets in the keychain; never in plain text; no custom authentication schemes.
- macOS: multiple people may be signed in; make no assumptions.

## Right to left ([reference](../references/foundations/right-to-left.md))

- Mirror the interface direction; align paragraphs by their language, not the UI direction; align list items consistently.
- Numerals keep their order within a number; sequences that show progress or counting flip as a whole.
- Flip controls that show progress or navigate fixed orders; keep controls that refer to a real direction or point at an onscreen area.
- Do not flip photos, artwork, logos, universal signs, or icons of real objects; do flip icons that represent text direction or forward and backward motion; localize icons that show text; consider complex icons part by part.

## SF Symbols ([reference](../references/foundations/sf-symbols.md))

- Rendering modes: monochrome, hierarchical, palette, multicolor; gradients (SF Symbols 7). Pick the mode that stays legible at the size and background in use.
- Variable color communicates change over time, not depth.
- Nine weights match SF text weights; three scales (small, medium, large) tune emphasis without breaking weight matching.
- Variants: outline (toolbars, lists), fill (iOS tab bars, swipe actions, accent-colored selection), slash (unavailable), enclosed (legibility at small sizes), language-specific variants.
- Animations: appear, disappear, bounce, scale, pulse, variable color, replace, magic replace, wiggle, breathe, rotate, draw on and off. Use judiciously, with a clear communicative purpose and a tone that fits the app.
- Custom symbols: start from a template, match system detail and weight, annotate layers, use negative margins when needed, use the component library for variants, provide alternative text, never replicate Apple products, never use SF Symbols in app icons or logos.

## Spatial layout (visionOS) ([reference](../references/foundations/spatial-layout.md))

- Center important content in the field of view; account for upright and angled viewing; never anchor to the head.
- Depth communicates hierarchy; avoid depth on text; make sure depth adds value and that cues communicate it accurately.
- Fixed scale for real-world objects, dynamic scale for legibility at distance.
- Few windows; indirect gestures first; the Digital Crown recenters; generous space around interactive items; usable with little or no movement; place large immersive experiences relative to the floor.

## Typography ([reference](../references/foundations/typography.md))

- Follow default and minimum sizes per platform; test legibility in context; avoid light weights.
- Convey hierarchy with weight, size, and color; minimize typefaces; keep hierarchy stable as text size changes; scale the content people care about, not every label.
- Use SF and New York via the system font APIs with the built-in text styles; modify with symbolic traits (bold, tight or loose leading) when needed; adjust tracking only in mockups.
- Custom fonts must be legible at the recommended sizes and implement Dynamic Type and Bold Text behavior.
- Dynamic Type: layouts adapt to all sizes, icons scale with text, minimal truncation, stacked layouts and fewer columns at large sizes, consistent hierarchy.
- macOS has no Dynamic Type; use the dynamic system font variants to match controls. visionOS: prefer 2D text, strong contrast, bold when text floats without a background, billboard text toward the viewer. watchOS: SF Compact, SF Compact Rounded in complications.

## Writing ([reference](../references/foundations/writing.md))

- Define the app's voice (vocabulary, feeling), then vary tone by situation (serious for errors and payments, light for achievements).
- Be clear and brief; cut every unneeded word; read it aloud. Write for everyone: plain language, no jargon, no gendered terms, localization-ready.
- Order each screen by importance; break multi-idea text across screens.
- Action-oriented labels: verbs on buttons and links ("Send", not "Let's do it!"; never "Click here").
- Build consistent language patterns and capitalization rules per element type (title case is formal, sentence case casual) and apply them everywhere. Multi-step flows: "Get Started" to begin, then a consistent "Continue" or "Next".
- Possessive pronouns sparingly ("Favorites", not "Your Favorites"); avoid "we".
- Use the right verb for the device: tap on touch devices, click with a pointer.
- Empty states explain what to do next. Error messages sit next to the problem, avoid blame, and say how to fix it ("Choose a password with at least 8 characters"); skip "Oops".
- Choose the delivery method by urgency (inline status, notification, alert). Settings labels describe the on state; link directly to a setting instead of describing its location. Text fields get clear labels and hint text ("name@example.com"), with errors shown beside the field.
