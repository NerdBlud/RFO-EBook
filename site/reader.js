const theme = document.querySelector("[data-theme-toggle]");
const systemTheme = matchMedia("(prefers-color-scheme: dark)");
const root = document.documentElement;
let done = {};

function readPreferences() {
  try {
    const savedTheme = localStorage.getItem("rfo-theme");
    if (savedTheme === "light" || savedTheme === "dark")
      root.dataset.theme = savedTheme;
    const savedProgress = JSON.parse(localStorage.getItem("rfo-done") || "{}");
    if (
      savedProgress &&
      typeof savedProgress === "object" &&
      !Array.isArray(savedProgress)
    ) {
      done = savedProgress;
    }
  } catch {
    // Keep the reader usable when storage is unavailable.
  }
}
readPreferences();

const isDark = () =>
  root.dataset.theme ? root.dataset.theme === "dark" : systemTheme.matches;
const updateThemeButton = () =>
  theme.setAttribute("aria-pressed", String(isDark()));
theme.hidden = false;
updateThemeButton();
systemTheme.addEventListener("change", updateThemeButton);
theme.addEventListener("click", () => {
  root.dataset.theme = isDark() ? "light" : "dark";
  try {
    localStorage.setItem("rfo-theme", root.dataset.theme);
  } catch {}
  updateThemeButton();
});

const refreshProgress = () => {
  let total = 0;
  for (const module of document.querySelectorAll("[data-module]")) {
    const rows = [...module.querySelectorAll("[data-lesson]")];
    const complete = rows.filter((row) => done[row.dataset.lesson] === true);
    for (const row of rows) {
      const checked = done[row.dataset.lesson] === true;
      row.classList.toggle("d", checked);
      const link = row.querySelector("a");
      if (checked)
        link.setAttribute(
          "aria-label",
          `${row.querySelector(".t").textContent} · Tamamlandı`,
        );
      else link.removeAttribute("aria-label");
    }
    const label = module.querySelector("[data-module-progress]");
    label.textContent = `${complete.length} / ${rows.length} tamamlanıb`;
    label.hidden = false;
    total += complete.length;
  }
  const progress = document.querySelector(".prog progress");
  if (progress) {
    progress.value = total;
    progress.previousElementSibling.textContent = `${total} / ${progress.max} dərs tamamlandı`;
    progress.closest(".prog").hidden = false;
  }
};
refreshProgress();

const complete = document.querySelector("[data-complete]");
if (complete) {
  const id = complete.dataset.complete;
  const refreshButton = () => {
    const checked = done[id] === true;
    complete.setAttribute("aria-pressed", String(checked));
    complete.textContent = checked ? "Tamamlandı ✓" : "Dərsi tamamla";
  };
  complete.hidden = false;
  refreshButton();
  complete.addEventListener("click", () => {
    done[id] = done[id] !== true;
    try {
      localStorage.setItem("rfo-done", JSON.stringify(done));
    } catch {}
    refreshButton();
  });
  addEventListener("pageshow", () => {
    readPreferences();
    refreshButton();
  });
}
addEventListener("pageshow", () => {
  readPreferences();
  updateThemeButton();
  refreshProgress();
});
