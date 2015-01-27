var converter = new Showdown.converter();
$(".code").each(function () {
    var markdown = $(this).html(),
           html;

    markdown = markdown.replace(/`{3}(\w+)\n/g, "<pre><code class='language-$1'>");
    markdown = markdown.replace(/`{3}\n/g, "</code></pre><br>");
    markdown = markdown.replace(/\n`{1}(.*)`{1}/g, "<br><pre><code class='language-python'>$1</code></pre><br>")
    markdown = markdown.replace(/`{1}([\w]*)`{1}/g, "<code class='language-python'>$1</code>");

   html = converter.makeHtml(markdown);

   $(this).empty().append(html);
});

Prism.highlightAll();
