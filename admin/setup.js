var PostPreview = createClass({
  render: function() {
    var entry = this.props.entry;

    return h("div", {},
      h("h1", {}, entry.getIn(["data", "title"])),
      h("h2", {}, entry.getIn(["data", "tagline"])),
      h("div", {"className": "text"}, this.props.widgetFor("body"))
    );
  }
});

CMS.registerPreviewTemplate("posts", PostPreview);
