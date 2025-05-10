public class Empleado {
    private String nombre;
    private String idEmpleado;
    private String cargo;

    public Empleado(String nombre, String idEmpleado, String cargo) {
        this.nombre = nombre;
        this.idEmpleado = idEmpleado;
        this.cargo = cargo;
    }

    public String getNombre() {
        return nombre;
    }

    public String getIdEmpleado() {
        return idEmpleado;
    }

    public String getCargo() {
        return cargo;
    }

    @Override
    public String toString() {
        return "Empleado [Nombre: " + nombre + ", ID: " + idEmpleado + ", Cargo: " + cargo + "]";
    }
}
