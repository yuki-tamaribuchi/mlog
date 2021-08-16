var object_name = document.currentScript.getAttribute('object_name');
var object_pk = document.currentScript.getAttribute('object_pk');
var function_name = document.currentScript.getAttribute('function_name');

window.opener[function_name](object_name,object_pk);
window.close();