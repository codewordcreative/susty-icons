# Sustainable UI icons
An initially small collection of sustainability-optimised SVG icons for free use and inspiration.

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
I'll cover this soon and link to it.

### More icons
Over time, I'll keep adding more

## How to contribute

### Ideas
If you have a pressing need for certain icons or noticed a particularly bad and commonly used one that needs some work, feel free to add a comment or an issue. I can't promise I'll be able to release one, but I can put it on the list. If others start contributing, perhaps someone else will take it up.

### Feedback / Tips
Very welcome. Reach out to me here or at my website, codewordcreative.com.

### Contributing
Very, very welcome. Ideally, reach out, so we can avoid doing the same work twice. I have a fair few icons in different stages of optimisation and can advice on the best approaches for consistency. Equally, I’m open to advice from others on improving my own work in this regard. I’m many things, but I’m not a trained designer.

## Attribution, forks, modification, licensing

I've deliberately used a permissive MIT License to encourage broad adoption of more sustainable icons everywhere. While not required under the MIT License, I’d still appreciate it if you could kindly credit me when redistributing these icons of modifications thereof, and or let me know if you’re redistributing them. To be honest, it’ll make me happy just to know more people are eager to rid the internet of inefficient icons.


