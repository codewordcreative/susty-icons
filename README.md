# Sustainable UI icons
An initially small collection of sustainability-optimised SVG icons for free use and inspiration.

## System and usage notes

### Styling
Colour and style are defined individually in the code. These are defauled to pure black (#000) for sustainability reasons. The viewbox is set to 160 x 160 to allow flexibility for more complex icons (see the comments on mathematics below). The stroke width is set to 5. You can play with all of these variables as you choose.

### External vs. inline use
Despite these being so small, external SVG files are recommended as they can be cached more easily and used across pages. There can be some sustainability advantages to inline SVGs in certain circumstances, but that’s beyond the scope of this project. Note that CSS cannot be used to manipulate elements of SVGs directly unless they are inline, although any manipulation you can apply to an image will work (though filters and transforms in CSS can have an impact, too).

### Summary of terms
This project uses an MIT licence. In short, reuse without attribution, even with modification, is fine in any personal or commercial project. Redistribution - read the licence for full details.

## Background

### There's a problem with most commonly used icons and SVGs
In short, many of the commonly used icon sets are not great on the sustainability front. Typical problems include:
* Multiple decimal places (computers don't like long multiplication and division any more than we do)
* Related: Irregular viewboxes
* Failure to use built-in shapes (e.g., circles, ellipses)
* Repeating identical or near-identical symbols more than once rather than using the symbol and use system
* Overuse of additional points to create curves, when adjusting the main curve would suffice
* General junk code, but existing tooling is good for getting rid of this
* Rare in icons, but worth mentioning: Some transforms used are much more complex to render (see below)

### Specifically: Code bloat 
Excessive data and unnecessarily information lead to code bloat. As in, more data transferred. This is often a matter of bytes, but this adds up fast in regularly used icons.

### Specifically: Rendering and resource usage 
The junk code is less of a problem than the rendering impact of unnecessarily complicated equations. Equally, some transforms are especially inefficient, for example, ones relating to lighting. Current tooling does not adequately account for the impact, but data will follow soon.

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

## How to contribute

### Ideas
If you have a pressing need for certain icons or noticed a particularly bad and commonly used one that needs some work, feel free to add a comment or an issue. I can't promise I'll be able to release one, but I can put it on the list. If others start contributing, perhaps someone else will take it up.

### Feedback / Tips
Very welcome. Reach out to me here or at my website, codewordcreative.com.

### Contributing
Very, very welcome. Ideally, reach out, so we can avoid doing the same work twice. I have a fair few icons in different stages of optimisation and can advice on the best approaches for consistency. Equally, I’m open to advice from others on improving my own work in this regard. I’m many things, but I’m not a trained designer.

## Attribution, forks, modification, licensing

I've deliberately used a permissive MIT License to encourage broad adoption of more sustainable icons everywhere. While not required under the MIT License, I’d still appreciate it if you could kindly credit me when redistributing these icons of modifications thereof, and or let me know if you’re redistributing them. To be honest, it’ll make me happy just to know more people are eager to rid the internet of inefficient icons.


