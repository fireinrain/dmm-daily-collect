import { request } from '@/utils'

export default {
  login: (data) => request.post('/base/access_token', data, { noNeedToken: true }),
  getUserInfo: () => request.get('/base/userinfo'),
  getUserMenu: () => request.get('/base/usermenu'),
  getUserApi: () => request.get('/base/userapi'),
  // profile
  updatePassword: (data = {}) => request.post('/base/update_password', data),
  // users
  getUserList: (params = {}) => request.get('/user/list', { params }),
  getUserById: (params = {}) => request.get('/user/get', { params }),
  createUser: (data = {}) => request.post('/user/create', data),
  updateUser: (data = {}) => request.post('/user/update', data),
  deleteUser: (params = {}) => request.delete(`/user/delete`, { params }),
  // role
  getRoleList: (params = {}) => request.get('/role/list', { params }),
  createRole: (data = {}) => request.post('/role/create', data),
  updateRole: (data = {}) => request.post('/role/update', data),
  deleteRole: (params = {}) => request.delete('/role/delete', { params }),
  updateRoleAuthorized: (data = {}) => request.post('/role/authorized', data),
  getRoleAuthorized: (params = {}) => request.get('/role/authorized', { params }),
  // menus
  getMenus: (params = {}) => request.get('/menu/list', { params }),
  createMenu: (data = {}) => request.post('/menu/create', data),
  updateMenu: (data = {}) => request.post('/menu/update', data),
  deleteMenu: (params = {}) => request.delete('/menu/delete', { params }),
  // apis
  getApis: (params = {}) => request.get('/api/list', { params }),
  createApi: (data = {}) => request.post('/api/create', data),
  updateApi: (data = {}) => request.post('/api/update', data),
  deleteApi: (params = {}) => request.delete('/api/delete', { params }),
  refreshApi: (data = {}) => request.post('/api/refresh', data),
  // depts
  getDepts: (params = {}) => request.get('/dept/list', { params }),
  createDept: (data = {}) => request.post('/dept/create', data),
  updateDept: (data = {}) => request.post('/dept/update', data),
  deleteDept: (params = {}) => request.delete('/dept/delete', { params }),
  // monitor
  getMonitors: (params = {}) => request.get('/monitor/list', { params }),
  createMonitor: (data = {}) => request.post('/monitor/create', data),
  updateMonitor: (data = {}) => request.post('/monitor/update', data),
  deleteMonitor: (params = {}) => request.delete('/monitor/delete', { params }),
  // monitor capture
  getMonitorSets: (params = {}) => request.get('/monitor/capture/list', { params }),
  createMonitorSet: (data = {}) => request.post('/monitor/capture/create', data),
  updateMonitorSet: (data = {}) => request.post('/monitor/capture/update', data),
  deleteMonitorSet: (params = {}) => request.delete('/monitor/capture/delete', { params }),
  refreshMonitorSet: (data = {}) => request.post('/monitor/capture/refresh', data),
  //monitor dash
  getMonitorSetsList: (params = {}) => request.get('/monitor/dash/list', { params }),
  getMonitorHisDetail: (params = {}) => request.get('/monitor/dash/detail', { params }),
  // dmm dmm-task
  getDmmTask: (params = {}) => request.get('/dmm/dmm-task/list', { params }),
  createDmmTask: (data = {}) => request.post('/dmm/dmm-task/create', data),
  updateDmmTask: (data = {}) => request.post('/dmm/dmm-task/update', data),
  deleteDmmTask: (params = {}) => request.delete('/dmm/dmm-task/delete', { params }),
  // dmm film-intro
  getFilmIntro: (params = {}) => request.get('/dmm/film-intro/list', { params }),
  createFilmIntro: (data = {}) => request.post('/dmm/film-intro/create', data),
  updateFilmIntro: (data = {}) => request.post('/dmm/film-intro/update', data),
  deleteFilmIntro: (params = {}) => request.delete('/dmm/film-intro/delete', { params }),

  // dmm film-detail
  getFilmDetail: (params = {}) => request.get('/dmm/film-detail/list', { params }),
  createFilmDetail: (data = {}) => request.post('/dmm/film-detail/create', data),
  updateFilmDetail: (data = {}) => request.post('/dmm/film-detail/update', data),
  deleteFilmDetail: (params = {}) => request.delete('/dmm/film-detail/delete', { params }),
  // dmm telegram-info
  getTelegramInfo: (params = {}) => request.get('/dmm/telegram-info/list', { params }),
  createTelegramInfo: (data = {}) => request.post('/dmm/telegram-info/create', data),
  updateTelegramInfo: (data = {}) => request.post('/dmm/telegram-info/update', data),
  deleteTelegramInfo: (params = {}) => request.delete('/dmm/telegram-info/delete', { params }),
}
