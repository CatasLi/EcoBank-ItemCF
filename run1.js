var exec = require('child_process').exec;
var filename = 'ItemCF1.py'
exec('python'+' '+filename,function(err,stdout,stderr){
    if(err)
    {
        console.log('stderr',err);
    }
    if(stdout)
    {
        console.log(stdout);
    }
});