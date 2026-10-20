# Download .net sdk image to container

# Working directory

# Copy everything

# Restore as distinct layers

# Build and publish a release

# Build runtime image



# Etapa final: usar Nginx para servir archivos estáticos
FROM nginx:alpine AS final
WORKDIR /usr/share/nginx/html

# Copy wwwroot and nginx configuration. Do not touch, please these two lines
COPY --from=build /TodoApp/TodoApp.Client/out/wwwroot .
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

