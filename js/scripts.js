const hamburger = document.querySelector(".hamburger");
    const navMenu = document.querySelector(".nav-menu");

    function toggleMenu() {
      document.getElementById('menu').classList.toggle('active');
  }

    hamburger.addEventListener("click", () => {
      hamburger.classList.toggle("active");
      navMenu.classList.toggle("active");
    });

    document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
      hamburger.classList.remove("active");
      navMenu.classList.remove("active");
    }));

// PDF.js 的 worker
pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.9.359/pdf.worker.min.js';

// 加載PDF
pdfjsLib.getDocument('https://drive.google.com/uc?export=download&id=1s7a5oHIOZ8l7_Fl_CGN76-UQlJ5uxs5B').promise.then(function(pdf) {
    // 獲取第一頁
    return pdf.getPage(1);
}).then(function(page) {
    var scale = 1.5;
    var viewport = page.getViewport({scale: scale});

    // 準備 canvas
    var canvas = document.createElement('canvas');
    var context = canvas.getContext('2d');
    canvas.height = viewport.height;
    canvas.width = viewport.width;

    // 渲染 PDF 頁面到 Canvas
    var renderContext = {
        canvasContext: context,
        viewport: viewport
    };
    page.render(renderContext);

    // 將 canvas 添加到網頁
    document.getElementById('pdf-viewer').appendChild(canvas);
}).catch(function(error) {
    console.error('Error loading PDF:', error);
    document.getElementById('pdf-viewer').textContent = 'Error loading PDF. Please try again later.';
});