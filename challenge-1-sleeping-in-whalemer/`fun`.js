module.exports = (w, h, we) => [true,false,undefined][/(?:f.t|(tff?$|(...?)))/.exec(`${w?"t":"f"}${h?"t":"f"}${we?"t":"f"}`).filter(a=>a===undefined).length];

//now this is a l g o r i t h m d e s i g n
