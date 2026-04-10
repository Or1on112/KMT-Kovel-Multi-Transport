# Design System Specification: Industrial Rationalism

## 1. Overview & Creative North Star

The Creative North Star for this design system is **"The Architectural Monolith."**

This system rejects the "bubbliness" of modern SaaS and the clutter of traditional industrial dashboards. Instead, it draws inspiration from Brutalist architecture and high-end editorial grid systems. We prioritize structural integrity, massive negative space, and a "Zero-Radius" philosophy. Every element is an intentional block of information, stacked with the precision of shipping containers.

To move beyond a "template" look, we utilize **Intentional Asymmetry**. Instead of centering content, we anchor it to a rigid, left-aligned grid with exaggerated margins (using the `24` spacing token), allowing the desaturated industrial imagery to act as a heavy visual counterweight.

---

## 2. Colors: Tonal Zoning

The palette is a spectrum of "Functional Greens." We do not use color for decoration; we use it to define "Zones" of infrastructure.

### The "No-Line" Rule

**Explicit Instruction:** Do not use 1px solid borders (`outline`) for sectioning. Structural boundaries must be defined solely through background color shifts. A section intended to stand out should move from `surface` to `surface-container-low`. The eye should perceive the change in "mass," not a thin line.

### Surface Hierarchy & Nesting

Treat the UI as a series of interlocking plates.

- **Base Level:** `surface` (#f7faf4)
- **Primary Workspaces:** `surface-container-low` (#f2f5ee)
- **Active Interactive Modules:** `surface-container-highest` (#e0e3dd)
- **The Grounding Element:** `inverse_surface` (#2d312d) for footers or high-impact sidebars.

### Textures & Polish

While the vibe is "no gradients," we apply a **"Micro-Texture"** approach. For high-conversion CTAs or Hero sections, use a subtle transition between `primary` (#005015) and `primary_container` (#006b1f) at a 45-degree angle to provide a "machined metal" finish that flat hex codes cannot replicate.

---

## 3. Typography: The Editorial Engine

We use a high-contrast scale to create an authoritative, "Blueprinted" feel.

- **Display (Manrope SemiBold):** Set at `display-lg` (3.5rem) with tight letter-spacing (-0.02em). Use this for core value propositions. It should feel heavy and unmovable.
- **Headlines (Manrope Bold):** Used for section headers. Always paired with large top margins (`spacing-16`) to let the "infrastructure" breathe.
- **Body (Inter Regular):** Set at `body-md` (0.875rem) for technical specs. The smaller font size against large margins creates a premium, technical-manual aesthetic.
- **Labels (Inter Medium):** Set at `label-md` (0.75rem). Use All-Caps for metadata and technical "Tags" to mimic industrial stamping.

---

## 4. Elevation & Depth: Tonal Layering

In this system, **shadows do not exist.** Depth is achieved through the **Layering Principle.**

- **The Physical Stack:** To "lift" a card, do not add a shadow. Instead, place a `surface-container-lowest` (#ffffff) block onto a `surface-container-high` (#e6e9e3) background. The 0px corners combined with the sharp color shift create a "clean-cut" depth.
- **The Ghost Border Fallback:** If accessibility requirements demand a container boundary on similar backgrounds, use the `outline_variant` (#bfcaba) at **15% opacity**. It should be felt, not seen.
- **Industrial Glass:** For navigation bars that overlay B&W imagery, use `surface` at 80% opacity with a `12px` backdrop blur. This ensures readability while maintaining the "Mist" atmospheric vibe.

---

## 5. Components: The Modular Units

### Buttons (The "Control Block")

- **Primary:** Background `primary`, Text `on_primary`, 0px border-radius. Padding: `spacing-4` (vertical) / `spacing-8` (horizontal).
- **Secondary:** Background `transparent`, Border `2px solid primary`, Text `primary`.
- **State:** On hover, shift background from `primary` to `deep_green`. No transitions; the change should be instant and mechanical.

### Cards & Lists

- **Rule:** Forbid divider lines.
- **Execution:** Separate list items using `spacing-4` vertical gaps. Use a subtle background shift (`surface-container-low`) on hover to indicate interactivity.

### Input Fields (The "Data Cell")

- **Visual:** A simple bottom-heavy block. Background `surface-container-highest`, 0px corners, no border except for a 2px `primary` underline on focus.
- **Labels:** Always place labels *above* the field in `label-sm` (All-Caps) using the `on_surface_variant` token.

### Industrial Status Chips

- **Selection:** Geometric rectangles. Use `secondary_fixed` for active states. Use `label-md` Inter Medium for the text.

---

## 6. Do's and Don'ts

### Do

- **Use Massive Margins:** If you think there is enough white space, add 20% more. Infrastructure needs room to scale.
- **B&W Imagery:** Only use high-contrast, desaturated industrial photography. If a photo has "natural" green, desaturate it to match the brand's `Industrial Green`.
- **Strict 0px Corners:** Every single element—buttons, inputs, cards, images—must have a hard 90-degree angle.

### Don't

- **Don't Use Shadows:** Not even "soft" ones. If an element needs to stand out, use a darker background zone.
- **Don't Use 1px Dividers:** They create visual "noise" that contradicts the "Simple & Rational" vibe. Use the Spacing Scale to create "Air Dividers."
- **Don't Use Centered Text:** Editorial layouts are built on the "Strong Left" line. Avoid centering headlines or body copy.

---

## 7. Signature Layout Patterns

- **The Split-Screen Hero:** 60% Width B&W Industrial Image / 40% Width Solid `Primary Green` Block with `Display-LG` white text.
- **The Data Grid:** Use `surface-container-low` for the header row and alternating `surface` / `surface-container-lowest` for data rows to create a "Zebra" effect without lines.
