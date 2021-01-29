CMS.registerPreviewStyle("/admin/style.css");

function extractArguments(s) {
  var matches = s.matchAll(/((?<key>\S+)="(?<value>[^"]+)")/g);

  var result = {}

  for (const match of matches) {
    result[match.groups.key] = match.groups.value
  }

  return result
}

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
CMS.registerPreviewTemplate("pages", PostPreview);

CMS.registerEditorComponent({
  id: "figure",
  label: "Figure",
  summary: "{{fields.caption}}",
  fields: [
    {
      name: "src",
      label: "File",
      widget: "image",
      media_library: {
        allow_multiple: false,
      },
    },
    {
      name: "alt",
      label: "Alt. Text",
      widget: "string",
    },
    {
      name: "caption",
      label: "Caption",
      widget: "string",
      required: false,
    },
    {
      name: "width",
      label: "Width",
      widget: "number",
      required: false,
      value_type: "string",
    },
    {
      name: "height",
      label: "Height",
      widget: "number",
      required: false,
      value_type: "string",
    },
  ],
  pattern: /^{{<[\s]?figure[\s]?([^}]+)[\s]?>}}$/,
  fromBlock: function(match) {
    return extractArguments(match[1]);
  },
  toBlock: function(obj) {
    return `{{< figure src="${obj.src || ""}" alt="${obj.alt || ""}" caption="${obj.caption || ""}" width="${obj.width || ""}" height="${obj.height || ""}" >}}`;
  },
  toPreview: function(obj, getAsset, fields) {
    var imageField = fields.find(f => f.get('widget') === 'image');
    var src = getAsset(obj.src, imageField);

    return `<figure><img src="${src || ""}" alt="${obj.alt || ""}" width="${obj.width || ""}" height="${obj.height || ""}"></img><figcaption>${obj.caption || ""}</figcaption></figure>`;
  }
});

CMS.registerEditorComponent({
  id: "youtube",
  label: "Youtube",
  fields: [
    {
      name: "id",
      label: "Video ID",
      hint: "dQw4w9WgXcQ",
      widget: "string",
    }
  ],
  pattern: /^{{<[\s]*youtube[\s]+id="(.*)"[\s]*>}}$/,
  fromBlock: function(match) {
    return {
      id: match[1],
    };
  },
  toBlock: function(obj) {
    return `{{< youtube id="${obj.id}" >}}`;
  },
  toPreview: function(obj) {
    return (
      `<iframe width="560" height="315" src="https://www.youtube.com/embed/${obj.id}" frameborder="0"></iframe>`
    );
  }
});

CMS.registerEditorComponent({
  id: "more",
  label: "More",
  pattern: `<!--more-->`,
  toBlock: function(obj) {
    return `<!--more-->`;
  },
  toPreview: function(obj) {
    return ``;
  }
});
