// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.hackerrank.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    window.onkeydown = function(event) {
       //Run button
   if (event.code === "F5") {
      document.getElementsByClassName("pull-right btn msR hr-monaco-compile")[0].click();
   }
       //Submit button
   else if (event.code === "F6") {
      document.getElementsByClassName(" pull-right btn btn-primary hr-monaco-submit")[0].click();
   }
   else if (event.code === "AltLeft") {
      document.getElementsByClassName("ui-btn ui-btn-normal fullscreen fullscreen-btn no-select active-link hr-monaco-base-btn")[0].click();
   }
};
})();