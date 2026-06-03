// Refresh the Google Scholar citation total and h-index on the homepage from
// assets/json/citations.json (updated periodically by a GitHub Action). The
// HTML ships with static fallback values, so on any failure we leave them be.
(function () {
  function apply(data) {
    if (!data) return;
    var link = document.querySelector('a[href*="scholar.google.com/citations"]');
    if (!link) return;
    var strongs = link.querySelectorAll("strong");
    if (strongs.length < 2) return;

    // First <strong> = total citations, second = h-index (see homepage markup).
    if (typeof data.total === "number" && data.total > 0) {
      strongs[0].textContent = data.total;
    }
    if (typeof data.h_index === "number" && data.h_index > 0) {
      strongs[1].textContent = data.h_index;
    }
  }

  function load() {
    fetch("/assets/json/citations.json", { cache: "no-cache" })
      .then(function (r) {
        return r.ok ? r.json() : null;
      })
      .then(apply)
      .catch(function () {
        /* keep the static fallback values */
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", load);
  } else {
    load();
  }
})();
