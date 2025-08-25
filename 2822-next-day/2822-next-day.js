/** 
 * @return {string}
 */
Date.prototype.nextDay = function() {
    const tom = this.getTime() + 24 * 60 * 60 * 1000
    return new Date(tom).toISOString().split("T")[0]
}

/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */