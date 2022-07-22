const passport = require('passport');

const local = require('./localStrategy');
const User = require('../models/user');

module.exports = () =>{
    passport.serializeUser((user, done)=>{ //user을 데이터화 시키겠다는 뜻
        done(null, user.id);
    });

    passport.deserializeUser((id, done) => {
        User.findOne({where : {id}})
        .then(user => done(null, user))
        .catch(err => done(err));
    });
    local();
};