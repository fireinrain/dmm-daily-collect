<script setup>
import { h, onMounted, ref, resolveDirective, withDirectives } from 'vue'
import { NButton, NForm, NFormItem, NInput, NPopconfirm, NDatePicker } from 'naive-ui'

import CommonPage from '@/components/page/CommonPage.vue'
import QueryBarItem from '@/components/query-bar/QueryBarItem.vue'
import CrudModal from '@/components/table/CrudModal.vue'
import CrudTable from '@/components/table/CrudTable.vue'
import TheIcon from '@/components/icon/TheIcon.vue'

import { renderIcon } from '@/utils'
import { useCRUD } from '@/composables'
// import { loginTypeMap, loginTypeOptions } from '@/constant/data'
import api from '@/api'

defineOptions({ name: '影片简介' })

const $table = ref(null)
const queryItems = ref({})
const vPermission = resolveDirective('permission')

const {
  modalVisible,
  modalTitle,
  modalLoading,
  handleSave,
  modalForm,
  modalFormRef,
  handleEdit,
  handleDelete,
  handleAdd,
} = useCRUD({
  name: '影片简介记录',
  initForm: {},
  doCreate: api.createFilmIntro,
  doUpdate: api.updateFilmIntro,
  doDelete: api.deleteFilmIntro,
  refresh: () => $table.value?.handleSearch(),
})
const handleEditWithDataConversion = (rowData) => {
  // Perform date string to date object conversion here
  const convertedData = {
    ...rowData,
  }

  // Pass the converted data to handleEdit function
  handleEdit(convertedData)
}

onMounted(() => {
  $table.value?.handleSearch()
})

const addFilmIntroRules = {
  film_title: [
    {
      required: true,
      message: '请输入影片标题',
      trigger: ['input', 'blur'],
    },
  ],
  film_star: [
    {
      required: true,
      message: '请输入影片演员',
      trigger: ['input', 'blur'],
    },
  ],
  film_price: [
    {
      required: true,
      message: '请输入影片价格',
      trigger: ['input', 'blur'],
    },
  ],
  film_cover_url: [
    {
      required: true,
      message: '请输入影片封面url',
      trigger: ['input', 'blur'],
    },
  ],
  film_detail_url: [
    {
      required: true,
      message: '请输入影片详情url',
      trigger: ['input', 'blur'],
    },
  ],
}

const columns = [
  {
    title: 'ID编号',
    key: 'id',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片标题',
    key: 'film_title',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片演员',
    key: 'film_star',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片价格',
    key: 'film_price',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '封面URL',
    key: 'film_cover_url',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '详情URL',
    key: 'film_detail_url',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '创建时间',
    key: 'created_at',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
    render(row) {
      return row.created_at
        ? new Date(row.created_at).toLocaleString('zh-CN', {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
          })
        : 'N/A'
    },
  },
  {
    title: '更新时间',
    key: 'updated_at',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
    render(row) {
      return row.updated_at
        ? new Date(row.updated_at).toLocaleString('zh-CN', {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
          })
        : 'N/A'
    },
  },
  {
    title: '操作',
    key: 'actions',
    width: 'auto',
    align: 'center',
    fixed: 'right',
    render(row) {
      return [
        withDirectives(
          h(
            NButton,
            {
              size: 'small',
              type: 'primary',
              style: 'margin-right: 8px;',
              onClick: () => {
                handleEditWithDataConversion(row)
              },
            },
            {
              default: () => '编辑',
              icon: renderIcon('material-symbols:edit', { size: 16 }),
            }
          ),
          [[vPermission, 'post/api/v1/dmm/film-intro/update']]
        ),
        h(
          NPopconfirm,
          {
            onPositiveClick: () => handleDelete({ film_intro_id: row.id }, false),
            onNegativeClick: () => {},
          },
          {
            trigger: () =>
              withDirectives(
                h(
                  NButton,
                  {
                    size: 'small',
                    type: 'error',
                  },
                  {
                    default: () => '删除',
                    icon: renderIcon('material-symbols:delete-outline', { size: 16 }),
                  }
                ),
                [[vPermission, 'delete/api/v1/dmm/film-intro/delete']]
              ),
            default: () => h('div', {}, '确定删除该历史记录吗?'),
          }
        ),
      ]
    },
  },
]
</script>

<template>
  <!-- 业务页面 -->
  <CommonPage show-footer title="影片简介列表">
    <template #action>
      <div>
        <NButton
          v-permission="'post/api/v1/dmm/film-intro/create'"
          class="float-right mr-15"
          type="primary"
          @click="handleAdd"
        >
          <TheIcon icon="material-symbols:add" :size="18" class="mr-5" />新建影片简介
        </NButton>
      </div>
    </template>
    <!-- 表格 -->
    <CrudTable
      ref="$table"
      v-model:query-items="queryItems"
      :columns="columns"
      :get-data="api.getFilmIntro"
    >
      <template #queryBar>
        <QueryBarItem label="影片标题" :label-width="60">
          <NInput
            v-model:value="queryItems.film_title"
            clearable
            type="text"
            placeholder="请输入影片标题"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="影片演员" :label-width="60">
          <NInput
            v-model:value="queryItems.film_star"
            clearable
            type="text"
            placeholder="请输入影片演员"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="影片价格" :label-width="60">
          <NInput
            v-model:value="queryItems.film_price"
            clearable
            type="text"
            placeholder="请输入影片价格"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
      </template>
    </CrudTable>

    <!-- 新增/编辑 弹窗 -->
    <CrudModal
      v-model:visible="modalVisible"
      :title="modalTitle"
      :loading="modalLoading"
      @save="handleSave"
    >
      <NForm
        ref="modalFormRef"
        label-placement="left"
        label-align="left"
        :label-width="80"
        :model="modalForm"
        :rules="addFilmIntroRules"
      >
        <NFormItem label="影片标题" path="film_title">
          <NInput v-model:value="modalForm.film_title" clearable placeholder="请输入影片标题" />
        </NFormItem>
        <NFormItem label="影片演员" path="film_star">
          <NInput v-model:value="modalForm.film_star" clearable placeholder="请输入影片演员" />
        </NFormItem>
        <NFormItem label="影片价格" path="film_price">
          <NInput v-model:value="modalForm.film_price" clearable placeholder="请输入影片价格" />
        </NFormItem>
        <NFormItem label="封面URL" path="film_cover_url">
          <NInput v-model:value="modalForm.film_cover_url" clearable placeholder="请输入封面URL" />
        </NFormItem>
        <NFormItem label="详情URL" path="film_detail_url">
          <NInput v-model:value="modalForm.film_detail_url" clearable placeholder="请输入详情URL" />
        </NFormItem>
      </NForm>
    </CrudModal>
  </CommonPage>
</template>
