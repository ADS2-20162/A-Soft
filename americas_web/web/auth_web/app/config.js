var baseUrl = 'http://localhost:9001/';
var loginUrl = 'http://localhost:9000/auth_web/';
var americasUrl = 'http://localhost:9000/americas_web/';

var client_id = 'UvGm0axuBetXP3FmsP8LQ3G6C5tyF8v9QRnLiti4';
var client_secret = 'Lk43okFaSjYJcxmCscb3tlR43rgj2Y9KgcXWLYCCsQ4U3D4ogv6qibVCEFu36xLeKs1PIn41hyYamu1Xg8Vzu3sNPRGbLfShXs6oHFhQqly72hELssUVbS79mFjd4LaH';
var grant_type = 'password';

var config = {
    baseUrl: baseUrl,
    loginUrl: loginUrl,
    americasUrl: americasUrl,

    client_id: client_id,
    client_secret: client_secret,
    grant_type: grant_type,
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