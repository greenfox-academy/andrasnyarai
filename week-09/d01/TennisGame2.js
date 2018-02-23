'use strict'

var TennisGame2 = function() {
  this.P1point = 0;
  this.P2point = 0;
  this.P1res;
  this.P2res;
  this.getScore = () => {
    let score = "";
  
    if (this.P1point === this.P2point) {
      if (this.P1point < 3) {
        if (this.P1point === 0) score = "Love";
        if (this.P1point === 1) score = "Fifteen";
        if (this.P1point === 2) score = "Thirty";
        score += "-All";
      } else if (this.P1point > 2) {
        score = "Deuce";
      }
    }
    if (this.P1point > 0 && this.P2point === 0) {
      this.P1res = "Fifteen";
      this.P2res = "Love";
    }
    if (this.P2point > 0 && this.P1point === 0) {
      this.P2res = "Fifteen";
      this.P1res = "Love";
    }
    if (this.P1point > this.P2point && this.P1point < 4) {
      if (this.P1point === 2) this.P1res = "Thirty";
      if (this.P1point === 3) this.P1res = "Forty";
      if (this.P2point === 1) this.P2res = "Fifteen";
      if (this.P2point === 2) this.P2res = "Thirty";
      score = this.P1res + "-" + this.P2res;
    }
    if (this.P2point > this.P1point && this.P2point < 4) {
      if (this.P2point === 2) this.P2res = "Thirty";
      if (this.P2point === 3) this.P2res = "Forty";
      if (this.P1point === 1) this.P1res = "Fifteen";
      if (this.P1point === 2) this.P1res = "Thirty";
      score = this.P1res + "-" + this.P2res;
    }
  
    if (this.P1point > this.P2point && this.P2point >= 3) {
      score = "Advantage player1";
    }
  
    if (this.P2point > this.P1point && this.P1point >= 3) {
      score = "Advantage player2";
    }
  
    if (this.P1point >= 4 && this.P2point >= 0 && (this.P1point - this.P2point) >= 2) {
      score = "Win for player1";
    }
    if (this.P2point >= 4 && this.P1point >= 0 && (this.P2point - this.P1point) >= 2) {
      score = "Win for player2";
    }
    return score;
  };
  
  this.P1Score = () => this.P1point++
  this.P2Score = () => this.P2point++
  this.wonPoint = (player) => {
    if (player === "player1") this.P1Score();
    else this.P2Score(); 
  }; 
};

if (typeof window === "undefined") {
  module.exports = TennisGame2;
}