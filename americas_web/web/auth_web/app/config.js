var baseUrl = 'http://localhost:9001/';
var loginUrl = 'http://localhost:9000/auth_web/';
var americasUrl = 'http://localhost:9000/americas_web/';

var clientId = 'Lhw3dGKyOtWIuf2gtEPJiLCb6Eyqsb6zEMuCmvai';
var clientSecret = '29PGN05H7JqpBUKKQmwp9JCUp7Qg8cVvWXSYIZRjI7Vu1pKNWZVXgVW9OtYJo1zVsMpxVOIZBKvYbkNArsh6mXcYaPZSkaRfgrzQwC2JllrEGRp4fL2XQo0WJCcZCJVm';
var grantType = 'password';

var config = {

    baseUrl: baseUrl,
    loginUrl: loginUrl,
    americasUrl: americasUrl,

    clientId: clientId,
    clientSecret: clientSecret,
    grantType: grantType,
};

app
    .value('config', config);

app
    .run(function($rootScope, $state, $stateParams, $window, loginService) {
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;

        /*******************************agregado**************************/
        console.log("run");

        if (loginService.authentication.isAuth === false) {
            $window.location = loginUrl;
        }
        /******************************************************************/
    })

.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    //$httpProvider.interceptors.push('authInterceptorService');
})

.config(function($resourceProvider) {
    // Don't strip trailing slashes from calculated URLs
    $resourceProvider.defaults.stripTrailingSlashes = false;
});
