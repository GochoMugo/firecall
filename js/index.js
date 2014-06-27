var converter = new Showdown.converter();
$(".markdown").each(function () {
    var markdown = $(this).html(),
           html;
    
    markdown = markdown.replace(/(\s+)\$\$end\$\$(\s+)/g, "$1</code>$2");       
   markdown = markdown.replace(/(\s+)\$\$([^\$]+)\$\$(\n?)(\s+)/g, "$1<code class='language-$2'>$3");
    
   markdown = markdown.replace(/(\s+)\$end\$(\s+)/g, "$1</code></pre>$2");       
   markdown = markdown.replace(/(\s+)\$([^\$]+)\$(\n?)(\s+)/g, "$1<pre><code class='language-$2'>$3");
   
   //markdown = markdown.replace(/<pre>(.*)\n([\s|\w|\W]*)<\/pre>/g, "<pre>$1<br>$2</pre>");
   html = converter.makeHtml(markdown);

   $("#" + $(this).attr("data-target")).append(html);
});

Prism.highlightAll();
