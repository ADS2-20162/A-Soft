app
    .controller('PersonCtrl', function($scope, $state, $stateParams,
        asociacionService, $window, $mdDialog, $log, toastr) {
        $scope.fields = 'name';
        var params = {};
        $scope.lista = [];
        $scope.person = {
            name: 'Asociacion',
            detail_name: 'Trabajar con personas',
            version: 'v1.0',
        };

        $scope.list = function(params) {
            $scope.isLoading = true;
            asociacionService.Person.query(params, function(r) {
                $scope.lista = r;
                $scope.isLoading = false;
            }, function(err) {
                $log.log("Error in list:" + JSON.stringify(err));
                toastr.error(err.data.results.detail, err.status + ' ' + err.statusText);
            });
        };

        $scope.list(params);

        /*   $scope.listCuentaBanco = function(i) {
               asociacionService.CuentaBanco.list({ cuenta_banco: i }).$promise.then(function(r) {
                   $scope.listaCuentaBanco = r;
               }, function(err) {
                   console.log("Err " + err);
               });
           };

           $scope.listCuentaBanco();*/

        $scope.buscar = function() {
            params.page = 1;
            params.fields = $scope.fields;
            params.query = $scope.query;
            $scope.list(params);
        };

        $scope.onReorder = function(order) {
            //Todo
            $log.log('Order: ' + order);
        };

        $scope.delete = function(d) {
            if ($window.confirm("Seguro?")) {
                asociacionService.Person.delete({ id: d.id }, function(r) {
                    $log.log("Se eliminó la persona:" + JSON.stringify(d));
                    toastr.success('Se eliminó la persona ' + d.ruc, 'Person');
                    $scope.list(params);
                }, function(err) {
                    $log.log("Error in delete:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            }
        };
    })
    .controller("PersonSaveCtrl", function($scope, $state, $stateParams,
        asociacionService, $window, $mdDialog, $log, toastr) {
        //Valores iniciales
        $scope.person = {
            name: 'Asociacion',
            detail_name: 'Agregando personas',
            version: 'v1.0',
        };

        $scope.sel = function() {
            asociacionService.Person.get({ id: $stateParams.id }, function(r) {
                $scope.person = r;
            }, function(err) {
                $log.log("Error in get:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        };
        if ($stateParams.id) {
            $scope.sel();
        }

        $scope.save = function() {
            if ($scope.person.id) {
                asociacionService.Person.update({ id: $scope.person.id }, $scope.person, function(r) {
                    $log.log("r: " + JSON.stringify(r));
                    toastr.success('Se editó la person ' + r.nombre, 'Person');
                    $state.go('asociacion.asociacion.persons');
                }, function(err) {
                    $log.log("Error in update:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            } else {
                asociacionService.Person.save($scope.person, function(r) {
                    $log.log("r: " + JSON.stringify(r));
                    toastr.success('Se insertó la person ' + r.nombre, 'Person');
                    $state.go('asociacion.asociacion.persons');
                }, function(err) {
                    $log.log("Error in save:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            }
        };

        $scope.cancel = function() {
            $state.go('asociacion.asociacion.persons');
        };
    });
