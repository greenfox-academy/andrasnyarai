'use strict'

var TennisGame3 = function(p1Name, p2Name) {
  this.p1 = 0;
  this.p2 = 0;
  this.p1Name = p1Name;
  this.p2Name = p2Name;
  this.getScore = () => {
    let s;
    if ((this.p1 < 4 && this.p2 < 4) && (this.p1 + this.p2 < 6)) {
      let p = ["Love", "Fifteen", "Thirty", "Forty"];
      s = p[this.p1];
      return (this.p1 == this.p2) ? s + "-All" : s + "-" + p[this.p2];
    } else {
      if (this.p1 == this.p2)
        return "Deuce";
      s = (this.p1 > this.p2) ? this.p1Name : this.p2Name;
      return ((this.p1 - this.p2) * (this.p1 - this.p2) == 1) ? "Advantage " + s : "Win for " + s;
    }
  }
  this.wonPoint = (playerName) => {
      if (playerName == "player1") this.p1 += 1;
      else this.p2 += 1;
  }
};

if (typeof window === "undefined") {
  module.exports = TennisGame3;
}