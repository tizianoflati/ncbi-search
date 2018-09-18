'use strict';

describe('Controller: DeleteProjectCtrl', function () {

  // load the controller's module
  beforeEach(module('sraSearchApp'));

  var DeleteProjectCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    DeleteProjectCtrl = $controller('DeleteProjectCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(DeleteProjectCtrl.awesomeThings.length).toBe(3);
  });
});