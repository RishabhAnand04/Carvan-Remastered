import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _793d7a62 = () => interopDefault(import('../pages/about.vue' /* webpackChunkName: "pages/about" */))
const _b0d98e60 = () => interopDefault(import('../pages/blog.vue' /* webpackChunkName: "pages/blog" */))
const _72989f62 = () => interopDefault(import('../pages/contact.vue' /* webpackChunkName: "pages/contact" */))
const _1fe5ecd8 = () => interopDefault(import('../pages/gallery.vue' /* webpackChunkName: "pages/gallery" */))
const _65f04ff0 = () => interopDefault(import('../pages/pricing.vue' /* webpackChunkName: "pages/pricing" */))
const _a51cbee8 = () => interopDefault(import('../pages/services.vue' /* webpackChunkName: "pages/services" */))
const _39cdc4d8 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/about",
    component: _793d7a62,
    name: "about"
  }, {
    path: "/blog",
    component: _b0d98e60,
    name: "blog"
  }, {
    path: "/contact",
    component: _72989f62,
    name: "contact"
  }, {
    path: "/gallery",
    component: _1fe5ecd8,
    name: "gallery"
  }, {
    path: "/pricing",
    component: _65f04ff0,
    name: "pricing"
  }, {
    path: "/services",
    component: _a51cbee8,
    name: "services"
  }, {
    path: "/",
    component: _39cdc4d8,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
