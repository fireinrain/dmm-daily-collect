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

defineOptions({ name: '电报信息' })

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
  name: '电报信息记录',
  initForm: {},
  doCreate: api.createTelegramInfo,
  doUpdate: api.updateTelegramInfo,
  doDelete: api.deleteTelegramInfo,
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

const addTelegramInfoRules = {
  telegraph_post_url: [
    {
      required: true,
      message: '请输入Telegraph链接',
      trigger: ['input', 'blur'],
    },
  ],
  film_detail_id: [
    {
      required: true,
      message: '请输入影片详情ID',
      trigger: ['input', 'blur'],
    },
  ],
  has_create_post: [
    {
      required: true,
      message: '请输入是否已创建Telegraph',
      trigger: ['input', 'blur'],
    },
  ],
  has_push_channel: [
    {
      required: true,
      message: '请输入是否已推送到TG频道',
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
    title: '影片详情ID',
    key: 'film_detail_id',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '创建Telegraph',
    key: 'has_create_post',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
    render(row) {
      return row.has_create_post ? '已创建' : '未创建'
    },
  },
  {
    title: '推送频道',
    key: 'has_push_channel',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
    render(row) {
      return row.has_push_channel ? '已推送' : '未推送'
    },
  },
  {
    title: 'Telegraph链接',
    key: 'telegraph_post_url',
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
          [[vPermission, 'post/api/v1/dmm/telegram-info/update']]
        ),
        h(
          NPopconfirm,
          {
            onPositiveClick: () => handleDelete({ telegram_info_id: row.id }, false),
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
                [[vPermission, 'delete/api/v1/dmm/telegram-info/delete']]
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
  <CommonPage show-footer title="电报信息列表">
    <template #action>
      <div>
        <NButton
          v-permission="'post/api/v1/dmm/telegram-info/create'"
          class="float-right mr-15"
          type="primary"
          @click="handleAdd"
        >
          <TheIcon icon="material-symbols:add" :size="18" class="mr-5" />
          新建电报信息
        </NButton>
      </div>
    </template>
    <!-- 表格 -->
    <CrudTable
      ref="$table"
      v-model:query-items="queryItems"
      :columns="columns"
      :get-data="api.getTelegramInfo"
    >
      <template #queryBar>
        <QueryBarItem label="影片详情ID" :label-width="60">
          <NInput
            v-model:value="queryItems.film_detail_id"
            clearable
            type="text"
            placeholder="请输入影片详情ID"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="已创建Telegraph" :label-width="90">
          <NInput
            v-model:value="queryItems.has_create_post"
            clearable
            type="text"
            placeholder="请输入是否创建Telegraph"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="已推送电报频道" :label-width="70">
          <NInput
            v-model:value="queryItems.has_push_channel"
            clearable
            type="text"
            placeholder="请输入是否推送频道"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="Telegraph链接" :label-width="70">
          <NInput
            v-model:value="queryItems.telegraph_post_url"
            clearable
            type="text"
            placeholder="请输入Telegraph链接"
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
        :rules="addTelegramInfoRules"
      >
        <NFormItem label="影片详情ID" path="film_detail_id">
          <NInput
            v-model:value="modalForm.film_detail_id"
            clearable
            placeholder="请输入影片详情ID"
          />
        </NFormItem>

        <NFormItem label="已创建Telegraph" path="has_create_post">
          <NInput
            v-model:value="modalForm.has_create_post"
            clearable
            placeholder="请输入已创建Telegraph"
          />
        </NFormItem>

        <NFormItem label="已推送频道" path="has_push_channel">
          <NInput
            v-model:value="modalForm.has_push_channel"
            clearable
            placeholder="请输入已推送频道"
          />
        </NFormItem>

        <NFormItem label="Telegraph链接" path="telegraph_post_url">
          <NInput
            v-model:value="modalForm.telegraph_post_url"
            clearable
            placeholder="请输入Telegraph链接"
          />
        </NFormItem>
      </NForm>
    </CrudModal>
  </CommonPage>
</template>
