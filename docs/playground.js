"use strict";

function updateCSSVars() {
  const root = document.documentElement;
  const el = (id) => document.getElementById(id);

  root.style.setProperty("--icon-size", el("iconSize").value + "px");
  root.style.setProperty("--stroke-width", el("strokeWidth").value);

  const stroke = el("strokeEnabled").checked ? el("strokeColour").value : "none";
  root.style.setProperty("--stroke-colour", stroke);

  root.style.setProperty("--bg-colour", el("bgColour").value);

  const fill = el("fillEnabled").checked ? el("fillColour").value : "none";
  root.style.setProperty("--fill-colour", fill);

  root.style.setProperty("--stroke-linecap", el("roundCaps").checked ? "round" : "butt");
  root.style.setProperty("--stroke-linejoin", el("roundJoins").checked ? "round" : "miter");

  el("sizeVal").textContent = el("iconSize").value;
  el("widthVal").textContent = el("strokeWidth").value;
  el("strokeColourVal").textContent = stroke;
  el("fillColourVal").textContent = fill;
  el("bgColourVal").textContent = el("bgColour").value;

  el("cssdisplay").textContent =
    `height: ${el("iconSize").value}px;` +
    `width: ${el("iconSize").value}px;` +
    `stroke-width: ${el("strokeWidth").value};` +
    `stroke: ${stroke};` +
    `fill: ${fill};` +
    `stroke-linecap: ${el("roundCaps").checked ? "round" : "butt"};` +
    `stroke-linejoin: ${el("roundJoins").checked ? "round" : "miter"};`;
}

window.addEventListener("DOMContentLoaded", () => {
  updateCSSVars();

  document.querySelectorAll(".controls input").forEach((input) =>
    input.addEventListener("input", updateCSSVars)
  );

  const lowData =
    navigator.connection?.saveData === true ||
    ["slow-2g", "2g"].includes(navigator.connection?.effectiveType);
  const prefersReducedData = window.matchMedia?.("(prefers-reduced-data: reduce)").matches;
  const ecoMode = document.documentElement.classList.contains("eco");

  if (lowData || prefersReducedData || ecoMode) {
    document
      .querySelectorAll('script[type="speculationrules"]')
      .forEach((el) => el.remove());
    console.log("Prefetch disabled: Low-data or eco mode rules applied.");
  }

  const tooltipToggle = document.getElementById("tooltipToggle");
  const tooltipContent = document.getElementById("tooltipContent");

  tooltipToggle?.addEventListener("click", (e) => {
    e.stopPropagation();
    const expanded = tooltipToggle.getAttribute("aria-expanded") === "true";
    tooltipToggle.setAttribute("aria-expanded", String(!expanded));
    tooltipContent.hidden = expanded;
  });

  document.addEventListener("click", (e) => {
    if (!tooltipContent.hidden) {
      tooltipToggle.setAttribute("aria-expanded", "false");
      tooltipContent.hidden = true;
    }
  });

  const copyCssBtn = document.getElementById("copy-css");
  const cssDisplay = document.getElementById("cssdisplay");

  copyCssBtn?.addEventListener("click", () => {
    if (cssDisplay) {
      navigator.clipboard.writeText(cssDisplay.textContent).then(() => {
        alert("CSS copied to clipboard!");
      }).catch((err) => {
        console.error("Failed to copy CSS:", err);
      });
    }
  });

  const updateThemeUI = (theme) => {
    document.getElementById("theme-light")?.setAttribute("aria-pressed", theme === "light");
    document.getElementById("theme-eco")?.setAttribute("aria-pressed", theme === "eco");
    document.getElementById("theme-dark")?.setAttribute("aria-pressed", theme === null);
  };

  const setTheme = (theme) => {
    document.documentElement.classList.remove("light", "eco");

    if (theme === "light" || theme === "eco") {
      document.documentElement.classList.add(theme);
      document.cookie = `theme=${theme}; path=/; max-age=31536000`;
    } else {
      document.cookie = "theme=; path=/; max-age=0";
    }

    updateThemeUI(theme);
  };

  document.getElementById("theme-light")?.addEventListener("click", () => setTheme("light"));
  document.getElementById("theme-eco")?.addEventListener("click", () => setTheme("eco"));
  document.getElementById("theme-dark")?.addEventListener("click", () => setTheme(null));
});
