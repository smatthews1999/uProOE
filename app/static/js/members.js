function VM() {
    var self = this;

    //self.memberList = ko.observableArray();
    self.srchLast = ko.observable();
    self.srchFirst = ko.observable();
    self.srchSSN = ko.observable();
    self.srchMID = ko.observable();

    self.search = function () {
        alert('searching');
    }
}

var vm = new VM();

ko.applyBindings(vm, document.getElementById("members_div"));