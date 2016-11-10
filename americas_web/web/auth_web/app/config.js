var baseUrl = 'http://localhost:9001/';
var loginUrl = 'http://localhost:9000/auth_web/';
var americasUrl = 'http://localhost:9000/americas_web/';

var clientId = 'p1LJXTD2qGhNvHaxBAozJ8gt2Rw7NqBqhsXPJ5FQ';
var clientSecret = 'u2q6c6TSyVYU69nPQJt0CjdZW0JHsdjtjzCPG6Ts8tIK1fYwgFWxaL2Mo6b7OhmKAoVkdcQ0sVA7AZ4C5PY1XGagcOcgScQg7OZTgFY6qYofO70WFGZXVFxovMnCiZA3';
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
