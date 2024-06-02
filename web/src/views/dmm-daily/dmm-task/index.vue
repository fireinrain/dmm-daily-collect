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

defineOptions({ name: '任务历史' })

const $table = ref(null)
const queryItems = ref({
  has_run: true,
})
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
  name: '任务历史',
  initForm: {},
  doCreate: api.createDmmTask,
  doUpdate: api.updateDmmTask,
  doDelete: api.deleteDmmTask,
  refresh: () => $table.value?.handleSearch(),
})
const handleEditWithDataConversion = (rowData) => {
  // Perform date string to date object conversion here
  const convertedData = {
    ...rowData,
    report_time: new Date(rowData.report_time).getTime(), // Convert reportTime to date object
    start_time: new Date(rowData.start_time).getTime(), // Convert startTime to date object
    end_time: new Date(rowData.end_time).getTime(), // Convert endTime to date object
  }

  // Pass the converted data to handleEdit function
  handleEdit(convertedData)
}

onMounted(() => {
  $table.value?.handleSearch()
})

const addDmmtaskRules = {
  fetch_url: [
    {
      required: true,
      message: '请输入任务URL',
      trigger: ['input', 'blur'],
    },
  ],
  has_run: [
    {
      required: true,
      message: '请输入是否已运行',
      trigger: ['input', 'blur'],
    },
  ],
  run_date: [
    {
      required: true,
      message: '请输入运行日期',
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
    title: '任务URL',
    key: 'fetch_url',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '是否运行',
    key: 'has_run',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
    render(row) {
      return row.has_run ? '已完成' : '未运行'
    },
  },
  {
    title: '运行日期',
    key: 'run_date',
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
          [[vPermission, 'post/monitor/v1/api/update']]
        ),
        h(
          NPopconfirm,
          {
            onPositiveClick: () => handleDelete({ monitor_id: row.id }, false),
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
                [[vPermission, 'delete/api/v1/monitor/delete']]
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
  <CommonPage show-footer title="任务历史列表">
    <template #action>
      <div>
        <NButton
          v-permission="'post/api/v1/dmm/dmm-task/create'"
          class="float-right mr-15"
          type="primary"
          @click="handleAdd"
        >
          <TheIcon icon="material-symbols:add" :size="18" class="mr-5" />新建任务历史
        </NButton>
      </div>
    </template>
    <!-- 表格 -->
    <CrudTable
      ref="$table"
      v-model:query-items="queryItems"
      :columns="columns"
      :get-data="api.getDmmTask"
    >
      <template #queryBar>
        <QueryBarItem label="已运行" :label-width="50">
          <NInput
            v-model:value="queryItems.has_run"
            clearable
            type="text"
            placeholder="请输入是否已运行(true/false)"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="运行日期" :label-width="60">
          <NDatePicker
            v-model:value="queryItems.run_date"
            clearable
            type="date"
            placeholder="请输入起始时间"
            @update:value="$table?.handleSearch()"
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
        :rules="addDmmtaskRules"
      >
        <NFormItem label="任务URL" path="sn">
          <NInput v-model:value="modalForm.fetch_url" clearable placeholder="请输入任务URL" />
        </NFormItem>
        <NFormItem label="是否已经运行" path="has_run">
          <NInput v-model:value="modalForm.has_run" clearable placeholder="请输入是否已经运行" />
        </NFormItem>
        <NFormItem label="运行日期" path="run_date">
          <NInput v-model:value="modalForm.run_date" clearable placeholder="请输入运行日期" />
        </NFormItem>
      </NForm>
    </CrudModal>
  </CommonPage>
</template>
