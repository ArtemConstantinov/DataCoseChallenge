FROM node:18.17-alpine3.17 AS base

ENV APP_ROOT /app
ENV HOST 0.0.0.0

RUN mkdir -p ${APP_ROOT} && \
    sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories && \
	echo "**** Install build packages ****" && \
    npm config set registry https://registry.npm.taobao.org/

WORKDIR ${APP_ROOT}


FROM base AS development

ENV NODE_ENV=development

COPY /package.json ${APP_ROOT}
# COPY /package-lock.json ${APP_ROOT}
RUN yarn install