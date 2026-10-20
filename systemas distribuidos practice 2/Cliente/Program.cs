using ClienteApp;
using Restaurante;

Console.WriteLine("╔════════════════════════════════════════════╗");
Console.WriteLine("║     CLIENTE DE RESTAURANTE - gRPC         ║");
Console.WriteLine("╚════════════════════════════════════════════╝\n");

var service = new RestauranteClienteService();

// Connect to server
service.ConnectAsync();
    
    bool running = true;
    while (running)
    {
        Console.WriteLine("\n┌─── MENÚ PRINCIPAL ───┐");
        Console.WriteLine("│ 1. Hacer pedido       │");
        Console.WriteLine("│ 2. Consultar estado   │");
        Console.WriteLine("│ 3. Salir              │");
        Console.WriteLine("└───────────────────────┘");
        
        Console.Write("\nSeleccione opción: ");
        string? option = Console.ReadLine();

        try
        {
            switch (option)
            {
                case "1":
                    await HacerPedido(service);
                    break;
                    
                case "2":
                    await ConsultarEstado(service);
                    break;
                    
                case "3":
                    running = false;
                    Console.WriteLine("\n¡Hasta luego!");
                    break;
                    
                default:
                    Console.WriteLine("Opción no válida");
                    break;
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"\n Error: {ex.Message}");
        }
    }

// ==================== MÉTODOS AUXILIARES ====================

async Task HacerPedido(RestauranteClienteService service)
{
    Console.WriteLine("\n--- CREAR NUEVO PEDIDO ---\n");
    
    var platos = new List<PlatoPedido>();
    bool agregandoPlatos = true;
    
    while (agregandoPlatos)
    {
        Console.Write("Nombre del plato (o presione Enter para terminar): ");
        string? nombrePlato = Console.ReadLine();
        
        if (string.IsNullOrWhiteSpace(nombrePlato))
        {
            agregandoPlatos = false;
            break;
        }
        
        Console.Write("Cantidad: ");
        if (int.TryParse(Console.ReadLine(), out int cantidad) && cantidad > 0)
        {
            platos.Add(new PlatoPedido { Nombre = nombrePlato, Cantidad = cantidad });
            Console.WriteLine($"Agregado: {cantidad}x {nombrePlato}");
        }
        else
        {
            Console.WriteLine("Cantidad no válida");
        }
    }
    
    if (platos.Count == 0)
    {
        Console.WriteLine("No se agregaron platos");
        return;
    }
    
    Console.Write("\nDistancia en km: ");
    if (!int.TryParse(Console.ReadLine(), out int distancia) || distancia < 0)
    {
        Console.WriteLine("Distancia no válida");
        return;
    }
    
    Console.WriteLine("\nEnviando pedido al restaurante...");
    await service.HacerPedidoAsync(platos, distancia);
}

async Task ConsultarEstado(RestauranteClienteService service)
{
    Console.WriteLine("\n--- CONSULTAR ESTADO DE PEDIDO ---\n");
    Console.Write("Ingrese el ID del pedido: ");
    
    if (!int.TryParse(Console.ReadLine(), out int idPedido) || idPedido <= 0)
    {
        Console.WriteLine("ID no válido");
        return;
    }
    
    await service.ConsultarEstadoPedidoAsync(idPedido);
}


