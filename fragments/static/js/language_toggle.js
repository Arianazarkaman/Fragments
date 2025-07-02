document.addEventListener('DOMContentLoaded', function () {
  const toggleBtn = document.getElementById('language-toggle-btn');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function (e) {
      e.preventDefault();
      console.log('Language toggle clicked');
      document.getElementById('language-toggle-form').submit();
    });
  }
});
