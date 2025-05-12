### A work in progress before initial release
Default: 5 point thickness stroke in 128 grid:
![Screenshot of currently finished icons](https://raw.githubusercontent.com/codewordcreative/susty-icons/refs/heads/main/sustyicons-grid.webp)
Thin variant: 2 point thickness stroke in 128 grid, found in subfolder:
![Screenshot of currently finished thin icons](https://raw.githubusercontent.com/codewordcreative/susty-icons/refs/heads/main/sustyicons-thin-grid.webp)
Light variant: Lighter stroke on dark background, found in subfolder:
![Screenshot of currently finished light icons](https://raw.githubusercontent.com/codewordcreative/susty-icons/refs/heads/main/sustyicons-light-grid.webp)

## Recent changes
Various new icons added. All icons standardised to a 128x128 grid. Padding standardised to 12 pixels. Sticking to pure line-icon style for maximum efficiency. I have now added a template icon (1template.svg) to allow anyone wishing to contribute their own icons to stick to the same styling. Note that this is prettified for clarity. I've also removed some unnecessary attributes (design-dependent). Python script to batch process SVGs to make changes across all created and tested - used to create the thin and light variants. It's very easy to create variant sets.

# Sustainable icons: The Susty Icons set
An initially small collection of sustainability-optimised SVG icons for free use and inspiration.

## What's so good about them

They're designed to be efficient in data size and rendering. They are significantly smaller than almost all icon sets out there right now, which is what necessitated their creation and sparked the desire to make this an MIT licence project.

## The alternative: HTML emojis

I'd be breaking a personal rule if I didn't mention this other option. This would be even more efficient than my SVGs. The problem is more consistency. If you can use HTML emojis, do. Add an aria-label if there is no accompanying text to explain what the symbol means.

## System and usage notes

### Styling
Colour and style are defined individually in the code. These are defaulted to pure black (#000). The viewbox is set to 128 x 128 to allow flexibility for more complex icons while supporting a common dimension (see the comments on mathematics below). The stroke width is set to 5. I’ve set fill to none (outline effect) and favoured a more rounded appearance to the lines. You can play with all of these variables as you choose.

### External vs. inline use
Despite these being so small, external SVG files are recommended as they can be cached more easily and used across pages. There can be some sustainability advantages to inline SVGs in certain circumstances, for example when only used once on a page or in combination with certain animations, but that’s beyond the scope of this project. Note that CSS cannot be used to manipulate elements of SVGs directly unless they are inline, although any manipulation you can apply to an image will work (though filters and transforms in CSS can have an impact, too).

### Accessibility
Currently, these icons have no title attribute. Ideally, you would add one in appropriate to the icon's purpose in your interface. Alternatively, alt text can help.

### Summary of terms
This project uses an MIT licence. In short, reuse without attribution, even with modification, is fine in any personal or commercial project. Redistribution - read the licence for full details.

## Background

### There's a problem with most commonly used icons and SVGs
In short, many of the commonly used icon sets are not great on the sustainability front. Typical problems include:
* Multiple decimal places (computers don't like long multiplication and division any more than we do)
* Related: Irregular viewboxes (but don't fudge that with lots of decimal places!)
* Failure to use built-in shapes (e.g., circles, ellipses)
* Outlining both sides of an outline icon's boundaries when the stroke-width attribute would suffice
* Repeating identical or near-identical symbols more than once rather than using the symbol and use system
* Overuse of additional points to create curves, when adjusting the main curve would suffice
* General junk code, but existing tooling is good for getting rid of this
* Unnecessary attributes (e.g., stroke-linejoin="round" in images where no lines join, or stroke-linecap="round" where no lines have open ends)
* Rare in icons, but worth mentioning: Some transforms used are much more complex to render (see below)
* Rare in icons, but common in logos: Forgetting the text element exists (vectors of text are so complex!)

### Additional aspect I'll be experimenting with
* Relative versus absolute positioning: While this won't make a difference in SVGs with a single starting position, it could play a role in others - increasing rendering complexity. This may have a negligible impact in small SVGs, but a bigger one in larger ones. Where there is no difference in data size, I am favouring absolute positioning.

### Specifically: Code bloat 
Excessive data and unnecessarily information lead to code bloat. As in, more data transferred. This is often a matter of bytes, but this adds up fast in regularly used icons.

### Specifically: Rendering and resource usage 
The junk code is less of a problem than the rendering impact of unnecessarily complicated equations. Equally, some transforms are especially inefficient, for example, ones relating to lighting. Current tooling does not adequately account for the impact, but data will follow soon.

### "Controversial" choice, at least for me...
I'm not putting the symbol inside <defs>. It can be read by modern browsers regardless and adds pointless bits. Better: I'll try to encourage colleagues at the W3C to update the standard. :)

### Why start with these?
I was inspired by a discussion on light, dark, and eco mode support for websites. Eco mode is currently not an option in browsers or systems, so it needs a UI solution. Dark and light mode are both still required for aesthetic and usability/accessibility requirements. I personally am in favour of not losing the option to switch manually. Then, in version 1.1 and beyond, I'm proceeding to add a few more commonly used icons.

#### Side note: Eco mode suggestions, in case the thought above intrigued you.
Pure black (#000) allows OLED monitors to completely cut power to those pixels. Green and red are more energy-efficient, while blue and white are worse. My own eco mode experiments use black backgrounds, green for text, and a lighter red for links. Red must usually be a bit brighter to still pass accessibility requirements. Use a contrast checker, e.g., https://webaim.org/resources/contrastchecker/

## What's next

### Blog post with a basic how I did this and how to
I’ll cover this soon and link to it.

### More icons
Over time, I’ll keep adding more. Hopefully others will join the cause.

### Potential improvements
Negative space variants. A different default colour. Thicker or thinner lines. I’ll probably look into this once I have made more, then I can automate the transformations and do them all at once with a script.

### One day, maybe
A generator with different styling options. Probably doable, but I’ll need to finish paid projects first!

### Caveat
I’m very new to Github, so bear with me if I do things in a strange way.

## How to do it

### Tools
It's low tech, because it needs the human eye. I use SVG Viewer (https://www.svgviewer.dev/) to see how I am doing and guide my adjustments. I insert my template (1template.svg) then play with the path using the SVG path editor (https://yqnn.github.io/svg-path-editor/) to ensure it's centred in a 128 x 128 grid with 12-point spacing. 

### Approaches
You can use the SVG path editor to clean up existing paths, play with size and rotation, round, and optimise. This is especially useful when ensuring a good fit in the grid. In general, you can go through the list of things I criticised in normal icons above. Cutting out unnecesary points. Working out how you can combine curves. Replacing complex curves with quadratic Bezier curves. Replacing straight 'curved' lines with curved lines. And when appropriate, also using reusable shapes and specific built-in shapes, such as circles. Try to favour absolute paths. The optimise function should be performed last. But note that it won't do more than the maths - and sometimes you'll need to check or correct how something rounded. Lastly, be sure to not include attributes you don't need in that design. As in, I use stroke-linecap="round" stroke-linejoin="round" in my icons, but not all icons need both to look correct.

### Warnings
Other tools will manipulate the icons when imported and exported again. On simpler icons, the impact may not be too big. My colleague and friend Nick Lewis tested the leaf icon (very simple) and the Github icon on Figma. The points themselves were changed in both cases, but the impact was minimal on the leaf. On the more detailed Github icon, however, there was a substantial increase in file size.

## How to contribute

### Ideas
If you have a pressing need for certain icons or noticed a particularly bad and commonly used one that needs some work, feel free to add a comment or an issue. I can't promise I'll be able to release one, but I can put it on the list. If others start contributing, perhaps someone else will take it up.

### Feedback / Tips
Very welcome. Reach out to me here or at my website, codewordcreative.com.

### Contributing
Very welcome. Ideally, reach out, so we can avoid doing the same work twice. I have a fair few icons in different stages of optimisation and can advise on the best approaches for consistency. Equally, I’m open to advice from others on improving my own work in this regard. I’m many things, but I’m not a trained designer.

## Attribution, forks, modification, licensing

I've deliberately used a permissive MIT License to encourage broad adoption of more sustainable icons everywhere. While not required under the MIT License, I’d still appreciate it if you could kindly credit me when redistributing these icons of modifications thereof, and or let me know if you’re redistributing them. To be honest, it’ll make me happy just to know more people are eager to rid the internet of inefficient icons. Added because of past experience with plagiarists: Obviously, you can't claim credit for creating them in the first place. I made them, and it took a lot of time and hyperfocus. Reuse, education, and learning from my techniques is encouraged. Deceptive behaviour is not.
