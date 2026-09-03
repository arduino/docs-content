"use strict";

module.exports = {
  names: ["no-h5-headings", "no-h5"],
  description: "Heading levels deeper than H4 (H5, H6) are not supported",
  tags: ["headings"],
  function: function rule(params, onError) {
    params.tokens
      .filter(function (token) { return token.type === "heading_open"; })
      .forEach(function (token) {
        if (token.tag === "h5" || token.tag === "h6") {
          onError({
            lineNumber: token.lineNumber,
            detail: "Heading level " + token.tag + " is not supported. Maximum allowed heading level is H4."
          });
        }
      });
  }
};
