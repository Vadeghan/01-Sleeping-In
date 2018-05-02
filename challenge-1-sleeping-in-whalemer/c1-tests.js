const si = require("./c1.js")

const ok = require('assert').ok;

ok(si(false, false) === true)
ok(si(true, false) === false)
ok(si(false, true) === true)

//ok(si(false, false, true) === true)
ok(si(true, false, true) === true)
ok(si(false, true, true) === undefined)
ok(si(false, false, true) === undefined)
