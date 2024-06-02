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

defineOptions({ name: '影片详情' })

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
  name: '影片详情记录',
  initForm: {},
  doCreate: api.createFilmDetail,
  doUpdate: api.updateFilmDetail,
  doDelete: api.deleteFilmDetail,
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

const addFilmDetailRules = {
  film_detail_url: [
    {
      required: true,
      message: '请输入影片详情URL',
      trigger: ['input', 'blur'],
    },
  ],
  film_pic_url: [
    {
      required: true,
      message: '请输入影片图片URL',
      trigger: ['input', 'blur'],
    },
  ],
  film_poster_url: [
    {
      required: true,
      message: '请输入影片海报URL',
      trigger: ['input', 'blur'],
    },
  ],
  film_title: [
    {
      required: true,
      message: '请输入影片标题',
      trigger: ['input', 'blur'],
    },
  ],
  film_publish_date: [
    {
      required: true,
      message: '请输入影片发布日期',
      trigger: ['input', 'blur'],
    },
  ],
  film_sell_date: [
    {
      required: true,
      message: '请输入影片销售日期',
      trigger: ['input', 'blur'],
    },
  ],
  film_length: [
    {
      required: true,
      message: '请输入影片时长',
      trigger: ['input', 'blur'],
    },
  ],
  film_stars: [
    {
      required: true,
      message: '请输入影片演员',
      trigger: ['input', 'blur'],
    },
  ],
  film_director: [
    {
      required: false,
      message: '请输入影片导演',
      trigger: ['input', 'blur'],
    },
  ],
  film_series: [
    {
      required: true,
      message: '请输入影片系列',
      trigger: ['input', 'blur'],
    },
  ],
  film_producers: [
    {
      required: true,
      message: '请输入影片制作人',
      trigger: ['input', 'blur'],
    },
  ],
  film_brand: [
    {
      required: true,
      message: '请输入影片品牌',
      trigger: ['input', 'blur'],
    },
  ],
  film_content_type: [
    {
      required: false,
      message: '请输入影片内容类型',
      trigger: ['input', 'blur'],
    },
  ],
  film_type: [
    {
      required: true,
      message: '请输入影片类型',
      trigger: ['input', 'blur'],
    },
  ],
  film_tags: [
    {
      required: true,
      message: '请输入影片标签',
      trigger: ['input', 'blur'],
    },
  ],
  film_code: [
    {
      required: true,
      message: '请输入影片编码',
      trigger: ['input', 'blur'],
    },
  ],
  film_desc: [
    {
      required: true,
      message: '请输入影片描述',
      trigger: ['input', 'blur'],
    },
  ],
  film_sample_image_prefix: [
    {
      required: true,
      message: '请输入影片样例图片前缀',
      trigger: ['input', 'blur'],
    },
  ],
  film_sample_images: [
    {
      required: true,
      message: '请输入影片样例图片',
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
    title: '影片销售日期',
    key: 'film_sell_date',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片时长',
    key: 'film_length',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片演员',
    key: 'film_stars',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片系列',
    key: 'film_series',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片制作人',
    key: 'film_producers',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片品牌',
    key: 'film_brand',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片编码',
    key: 'film_code',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片详情URL',
    key: 'film_detail_url',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '影片海报URL',
    key: 'film_poster_url',
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
          [[vPermission, 'post/api/v1/dmm/film-detail/update']]
        ),
        h(
          NPopconfirm,
          {
            onPositiveClick: () => handleDelete({ film_detail_id: row.id }, false),
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
                [[vPermission, 'delete/api/v1/dmm/film-detail/delete']]
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
          v-permission="'post/api/v1/dmm/film-detail/create'"
          class="float-right mr-15"
          type="primary"
          @click="handleAdd"
        >
          <TheIcon icon="material-symbols:add" :size="18" class="mr-5" />
          新建影片详情
        </NButton>
      </div>
    </template>
    <!-- 表格 -->
    <CrudTable
      ref="$table"
      v-model:query-items="queryItems"
      :columns="columns"
      :get-data="api.getFilmDetail"
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
        <QueryBarItem label="发售日期" :label-width="60">
          <NInput
            v-model:value="queryItems.film_sell_date"
            clearable
            type="text"
            placeholder="请输入发售日期"
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
        <QueryBarItem label="影片番号" :label-width="60">
          <NInput
            v-model:value="queryItems.film_code"
            clearable
            type="text"
            placeholder="请输入影片番号"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="影片标签" :label-width="60">
          <NInput
            v-model:value="queryItems.film_tags"
            clearable
            type="text"
            placeholder="请输入影片标签"
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
        :rules="addFilmDetailRules"
      >
        <NFormItem label="影片标题" path="film_title">
          <NInput v-model:value="modalForm.film_title" clearable placeholder="请输入影片标题" />
        </NFormItem>
        <NFormItem label="影片发布日期" path="film_publish_date">
          <NInput
            v-model:value="modalForm.film_publish_date"
            clearable
            placeholder="请输入影片发布日期"
          />
        </NFormItem>
        <NFormItem label="影片销售日期" path="film_sell_date">
          <NInput
            v-model:value="modalForm.film_sell_date"
            clearable
            placeholder="请输入影片销售日期"
          />
        </NFormItem>
        <NFormItem label="影片时长" path="film_length">
          <NInput v-model:value="modalForm.film_length" clearable placeholder="请输入影片时长" />
        </NFormItem>
        <NFormItem label="影片演员" path="film_stars">
          <NInput v-model:value="modalForm.film_stars" clearable placeholder="请输入影片演员" />
        </NFormItem>
        <NFormItem label="影片导演" path="film_director">
          <NInput v-model:value="modalForm.film_director" clearable placeholder="请输入影片导演" />
        </NFormItem>
        <NFormItem label="影片系列" path="film_series">
          <NInput v-model:value="modalForm.film_series" clearable placeholder="请输入影片系列" />
        </NFormItem>
        <NFormItem label="影片制作人" path="film_producers">
          <NInput
            v-model:value="modalForm.film_producers"
            clearable
            placeholder="请输入影片制作人"
          />
        </NFormItem>
        <NFormItem label="影片品牌" path="film_brand">
          <NInput v-model:value="modalForm.film_brand" clearable placeholder="请输入影片品牌" />
        </NFormItem>
        <NFormItem label="影片内容类型" path="film_content_type">
          <NInput
            v-model:value="modalForm.film_content_type"
            clearable
            placeholder="请输入影片内容类型"
          />
        </NFormItem>
        <NFormItem label="影片类型" path="film_type">
          <NInput v-model:value="modalForm.film_type" clearable placeholder="请输入影片类型" />
        </NFormItem>
        <NFormItem label="影片标签" path="film_tags">
          <NInput v-model:value="modalForm.film_tags" clearable placeholder="请输入影片标签" />
        </NFormItem>
        <NFormItem label="影片编码" path="film_code">
          <NInput v-model:value="modalForm.film_code" clearable placeholder="请输入影片编码" />
        </NFormItem>
        <NFormItem label="影片描述" path="film_desc">
          <NInput v-model:value="modalForm.film_desc" clearable placeholder="请输入影片描述" />
        </NFormItem>
        <NFormItem label="影片样例图片前缀" path="film_sample_image_prefix">
          <NInput
            v-model:value="modalForm.film_sample_image_prefix"
            clearable
            placeholder="请输入影片样例图片前缀"
          />
        </NFormItem>
        <NFormItem label="影片样例图片" path="film_sample_images">
          <NInput
            v-model:value="modalForm.film_sample_images"
            clearable
            placeholder="请输入影片样例图片"
          />
        </NFormItem>
        <NFormItem label="影片图片URL" path="film_pic_url">
          <NInput
            v-model:value="modalForm.film_pic_url"
            clearable
            placeholder="请输入影片图片URL"
          />
        </NFormItem>
        <NFormItem label="影片海报URL" path="film_poster_url">
          <NInput
            v-model:value="modalForm.film_poster_url"
            clearable
            placeholder="请输入影片海报URL"
          />
        </NFormItem>
        <NFormItem label="影片详情URL" path="film_detail_url">
          <NInput
            v-model:value="modalForm.film_detail_url"
            clearable
            placeholder="请输入影片详情URL"
          />
        </NFormItem>
      </NForm>
    </CrudModal>
  </CommonPage>
</template>
