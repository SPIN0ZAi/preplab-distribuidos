using System.Net.Http.Json;
using TodoApp.Client.Models;

namespace TodoApp.Client.Services;

public class TodoService
{
    private readonly HttpClient _httpClient;

    public TodoService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<List<Todo>> GetAllTodosAsync()
    {
        return await _httpClient.GetFromJsonAsync<List<Todo>>("/todoitems") ?? new List<Todo>();
    }

    public async Task<List<Todo>> GetCompleteTodosAsync()
    {
        return await _httpClient.GetFromJsonAsync<List<Todo>>("/complete") ?? new List<Todo>();
    }

    public async Task<Todo?> GetTodoAsync(int id)
    {
        return await _httpClient.GetFromJsonAsync<Todo>($"/{id}");
    }

    public async Task<Todo?> CreateTodoAsync(Todo todo)
    {
        var response = await _httpClient.PostAsJsonAsync("", todo);
        return response.IsSuccessStatusCode ? await response.Content.ReadFromJsonAsync<Todo>() : null;
    }

    public async Task<bool> UpdateTodoAsync(Todo todo)
    {
        var response = await _httpClient.PutAsJsonAsync($"/{todo.Id}", todo);
        return response.IsSuccessStatusCode;
    }

    public async Task<bool> DeleteTodoAsync(int id)
    {
        var response = await _httpClient.DeleteAsync($"/{id}");
        return response.IsSuccessStatusCode;
    }
}